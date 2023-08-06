import os
import traceback

import hypertrace.agent.filter
from hypertrace.agent.filter.registry import TYPE_HTTP, TYPE_RPC
from opentelemetry.trace import Span
from traceableai.config.config import Config
from hypertrace.agent.custom_logger import get_custom_logger # pylint:disable=C0413,C0411,C0412

logger = get_custom_logger(__name__)

_LIBTRACEABLE_AVAILABLE = False
_NOT_BODY = False
_IS_BODY = True

try:
    import traceableai.filter._libtraceable as _libtraceable  # pylint: disable=E0611,E0401,bad-option-value
    _LIBTRACEABLE_AVAILABLE = True
except Exception as error:  # pylint: disable=broad-except
    _LIBTRACEABLE_AVAILABLE = False
    traceback.print_tb(error.__traceback__)
    logger.warning(error)
    logger.warning(
        "error loading traceable extension - libtraceable filter disabled")


_HEADER_PREFIXES = {
    TYPE_HTTP: 'http.request.header',
    TYPE_RPC: 'rpc.request.metadata'
}

_BODY_PREFIXES = {
    TYPE_HTTP: 'http.request.body',
    TYPE_RPC: 'rpc.request.body'
}


class Traceable(hypertrace.agent.filter.Filter):

    def __init__(self):
        if _LIBTRACEABLE_AVAILABLE:
            self.libtraceable_config = _create_libtraceable_config()
            p_libtraceable = _libtraceable.ffi.new("traceable_libtraceable*")
            result_code = _libtraceable.lib.traceable_new_libtraceable(
                self.libtraceable_config, p_libtraceable)
            self.libtraceable_available = (
                result_code == _libtraceable.lib.TRACEABLE_SUCCESS)
            if self.libtraceable_available:
                logger.debug("libtraceable available")
                self.libtraceable = p_libtraceable[0]
                result = _libtraceable.lib.traceable_start_libtraceable(
                    self.libtraceable)
                if result != _libtraceable.lib.TRACEABLE_SUCCESS:
                    logger.debug("Failed to start libtraceable")
                    self.libtraceable_available = False
        else:
            self.libtraceable_available = False

    def evaluate_url_and_headers(self, span: Span, url: str, headers: dict, request_type) -> bool:
        if not self.libtraceable_available:
            return False

        pairs = _add_header_and_span_attributes(span, headers, request_type)

        # add url as part of header processing
        pairs.append((_libtraceable.ffi.new("char[]", b"http.url"),
                      _libtraceable.ffi.new("char[]", f"{url}".encode('ascii'))))

        num_headers = len(pairs)
        attributes = _libtraceable.ffi.new("traceable_attributes*")
        attribute_array = _libtraceable.ffi.new(
            "traceable_attribute[]", num_headers)
        attributes.count = num_headers

        for index, pair in enumerate(pairs, start=0):
            attribute_array[index].key = pair[0]
            attribute_array[index].value = pair[1]
        attributes.attribute_array = attribute_array

        return self._evaluate_attributes(span, attributes, _NOT_BODY)

    def evaluate_body(self, span: Span, body, headers: dict, request_type) -> bool:
        if not self.libtraceable_available:
            return False

        if not body or len(str(body)) == 0:
            return False

        pairs = _add_header_and_span_attributes(span, headers, request_type)
        prefix = _BODY_PREFIXES[request_type]
        try:
            if isinstance(body, bytes):
                pairs.append((_libtraceable.ffi.new("char[]", prefix.encode('ascii')),
                              _libtraceable.ffi.new("char[]", body)))
            else:
                pairs.append((_libtraceable.ffi.new("char[]", prefix.encode('ascii')),
                              _libtraceable.ffi.new("char[]", f"{body}".encode('ascii'))))
        except Exception as exception: # pylint:disable=W0703
            logger.error("Error adding body data to extension call: %s", exception)

        num_attrs = len(pairs)
        attributes = _libtraceable.ffi.new("traceable_attributes*")
        attribute_array = _libtraceable.ffi.new(
            "traceable_attribute[]", num_attrs)
        attributes.count = num_attrs

        for index, pair in enumerate(pairs, start=0):
            attribute_array[index].key = pair[0]
            attribute_array[index].value = pair[1]
        attributes.attribute_array = attribute_array

        return self._evaluate_attributes(span, attributes, _IS_BODY)

    def _evaluate_attributes(self, span, attributes, is_body) -> bool:
        result = _libtraceable.ffi.new("traceable_process_request_result*")
        result_code = _libtraceable.lib.TRACEABLE_SUCCESS
        if is_body:
            result_code = _libtraceable.lib.traceable_process_request_body(
                self.libtraceable, attributes[0], result)  # pylint:disable=C0301
        else:
            result_code = _libtraceable.lib.traceable_process_request_headers(
                self.libtraceable, attributes[0], result)

        if result_code != _libtraceable.lib.TRACEABLE_SUCCESS:
            logger.debug("traceable_process_request fail!")
            return False

        _add_span_attributes(span, result)

        _result_code = _libtraceable.lib.traceable_delete_process_request_result_data(
            result[0])
        if result.block:
            return True
        return False


def _add_span_attributes(span: Span, process_request_result):
    attr_count = process_request_result.attributes.count
    for i in range(attr_count):
        key_attr = process_request_result.attributes.attribute_array[i].key
        value_attr = process_request_result.attributes.attribute_array[i].value
        if key_attr == _libtraceable.ffi.NULL or value_attr == _libtraceable.ffi.NULL:
            continue

        key = _libtraceable.ffi.string(key_attr)
        value = _libtraceable.ffi.string(value_attr)

        span.set_attribute(key.decode('utf-8', 'backslashescape'),
                           value.decode('utf-8', 'backslashescape'))


def _add_header_and_span_attributes(span: Span, headers: dict, request_type) -> []:
    pairs = []
    ip_address = span._readable_span().attributes.get('net.peer.ip')  # pylint:disable=W0212
    if ip_address:
        pairs.append((_libtraceable.ffi.new("char[]", b"net.peer.ip"),
                      _libtraceable.ffi.new("char[]", f"{ip_address}".encode('ascii'))))

    header_prefix = _HEADER_PREFIXES[request_type]
    for header_key, header_value in headers.items():
        pairs.append((_libtraceable.ffi.new("char[]", f"{header_prefix}.{header_key}".lower().encode('ascii')),
                      _libtraceable.ffi.new("char[]", f"{header_value}".encode('ascii'))))

    return pairs


def _create_libtraceable_config():
    traceable_config = Config().config
    should_debug = 0
    if os.environ.get("TA_LOG_LEVEL", "").upper() == "DEBUG":
        should_debug = 1
    if traceable_config.blocking_config.debug_log.value is True:
        should_debug = 1

    libtraceable_config = _libtraceable.lib.init_libtraceable_config()

    libtraceable_config.log_config.mode = should_debug

    # If blocking is disabled we will never attempt to initialize the traceable filter
    # so we can safely set to 1 here
    libtraceable_config.blocking_config.enabled = 1

    traceable_opa = traceable_config.opa
    opa_server_url = _libtraceable.ffi.new(
        "char[]", f"{traceable_opa.endpoint.value}".encode('ascii'))

    opa_enabled = (0 if not traceable_opa.enabled.value is True else 1)
    libtraceable_config.blocking_config.opa_config.enabled = opa_enabled
    libtraceable_config.blocking_config.opa_config.opa_server_url = opa_server_url
    libtraceable_config.blocking_config.opa_config.log_to_console = 1
    libtraceable_config.blocking_config.opa_config.debug_log = should_debug
    libtraceable_config.blocking_config.opa_config.min_delay = traceable_opa.poll_period_seconds.value
    libtraceable_config.blocking_config.opa_config.max_delay = traceable_opa.poll_period_seconds.value

    modsecurity_enabled = (
        1 if traceable_config.blocking_config.modsecurity.enabled.value is True else 0)

    libtraceable_config.blocking_config.modsecurity_config.enabled = modsecurity_enabled

    rb_enabled = 1 if traceable_config.blocking_config.region_blocking.enabled.value is True else 0
    libtraceable_config.blocking_config.rb_config.enabled = rb_enabled

    libtraceable_config.blocking_config.evaluate_body = (
        1 if traceable_config.blocking_config.evaluate_body.value is True else 0)
    libtraceable_config.blocking_config.skip_internal_request = (
        1 if traceable_config.blocking_config.skip_internal_request.value is True else 0)  # pylint:disable=C0301

    remote_config_enabled = (
        1 if traceable_config.blocking_config.remote_config.enabled.value is True else 0)
    libtraceable_config.remote_config.enabled = remote_config_enabled

    cert_file = _libtraceable.ffi.new("char[]", "".encode('ascii'))
    libtraceable_config.remote_config.cert_file = cert_file

    remote_config_endpoint = (
        traceable_config.blocking_config.remote_config.endpoint.value)
    remote_url = _libtraceable.ffi.new(
        "char[]", f"{remote_config_endpoint}".encode('ascii'))
    libtraceable_config.remote_config.remote_endpoint = remote_url

    remote_poll_period_seconds = (
        traceable_config.blocking_config.remote_config.poll_period_seconds.value)
    libtraceable_config.remote_config.poll_period_sec = remote_poll_period_seconds

    service_name = _libtraceable.ffi.new( "char[]", "".encode('ascii'))
    libtraceable_config.agent_config.service_name = service_name
    return libtraceable_config
