from traceableai.config import traceable_hypertrace_config


# To simplify usage for end users
# we bundle the traceable & hypertrace configs into a single dict
# Then once modifications are complete, apply the dict values back onto the original protobuf
# the primary benefit is users no longer have to use protobuf fields/values and can modify the config with primitives
# Additionally we don't have to expose the 2 configs independently, instead they are yielded as a single config
class ConfigWrapper:  # pylint:disable=R0903
    def __init__(self, ht_config, ta_config):
        self.traceable = ta_config
        self.hypertrace = ht_config

    def apply_modifications(self, modified_config_dict):
        # blocking config
        self.traceable.blocking_config.enabled.value = modified_config_dict["blocking_config"]["enabled"]
        self.traceable.blocking_config.debug_log.value = modified_config_dict["blocking_config"]["debug_log"]
        self.traceable.blocking_config.evaluate_body.value = modified_config_dict["blocking_config"]["evaluate_body"]
        self.traceable.blocking_config.modsecurity.enabled.value = \
            modified_config_dict["blocking_config"]["modsecurity"]["enabled"]
        self.traceable.blocking_config.skip_internal_request.value = \
            modified_config_dict["blocking_config"]["skip_internal_request"]
        self.traceable.blocking_config.region_blocking.enabled.value = \
            modified_config_dict["blocking_config"]["region_blocking"]["enabled"]
        self.traceable.blocking_config.remote_config.enabled.value = \
            modified_config_dict["blocking_config"]["remote_config"]["enabled"]
        self.traceable.blocking_config.remote_config.endpoint.value =\
            modified_config_dict["blocking_config"]["remote_config"]["endpoint"]
        self.traceable.blocking_config.remote_config.poll_period_seconds.value = \
            modified_config_dict["blocking_config"]["remote_config"]["poll_period_seconds"]
        # opa
        self.traceable.opa.enabled.value = modified_config_dict["opa"]["enabled"]
        self.traceable.opa.endpoint.value = modified_config_dict["opa"]["endpoint"]
        self.traceable.opa.poll_period_seconds.value = modified_config_dict["opa"]["poll_period_seconds"]

        # hypertrace top level
        self.hypertrace.enabled = modified_config_dict["enabled"]
        self.hypertrace.service_name = modified_config_dict["service_name"]

        proto_propagation_formats = []
        for prop_format in modified_config_dict["propagation_formats"]:
            proto_propagation_formats.append(traceable_hypertrace_config.PropagationFormat.Value(prop_format))
        self.hypertrace.propagation_formats = proto_propagation_formats

        # reporting
        reporting = modified_config_dict["reporting"]
        self.hypertrace.reporting.endpoint = reporting["endpoint"]
        self.hypertrace.reporting.secure = reporting["secure"]
        self.hypertrace.reporting.trace_reporter_type = \
            traceable_hypertrace_config.TraceReporterType.Value(reporting["trace_reporter_type"])

        # data capture
        data_capture = modified_config_dict["data_capture"]
        self.hypertrace.data_capture.http_headers.request.value = data_capture["http_headers"]["request"]
        self.hypertrace.data_capture.http_headers.response.value = data_capture["http_headers"]["response"]
        self.hypertrace.data_capture.http_body.request.value = data_capture["http_body"]["request"]
        self.hypertrace.data_capture.http_body.response.value = data_capture["http_body"]["response"]
        self.hypertrace.data_capture.rpc_metadata.request.value = data_capture["rpc_metadata"]["request"]
        self.hypertrace.data_capture.rpc_metadata.response.value = data_capture["rpc_metadata"]["response"]
        self.hypertrace.data_capture.rpc_body.request.value = data_capture["rpc_body"]["request"]
        self.hypertrace.data_capture.rpc_body.response.value = data_capture["rpc_body"]["response"]
        self.hypertrace.data_capture.body_max_size_bytes = data_capture["body_max_size_bytes"]

    def current_config(self):
        # We should revisit the Hypertrace config loader, current it prevents us from doing:
        # MessageToDict(ht_config)
        # Then this could become:
        # current_config = {}.merge(MessageToDict(ht_config).merge(MessageToDict(ta_config))
        # Similar in apply modifications we could then just use AgentConfig.CopyFrom
        propagation_formats = []
        for prop_format in self.hypertrace.propagation_formats:
            propagation_formats.append(traceable_hypertrace_config.PropagationFormat.Name(prop_format))

        return {
            'enabled': self.hypertrace.enabled,
            'propagation_formats': propagation_formats,
            'service_name': self.hypertrace.service_name,
            'reporting': {
                'endpoint': self.hypertrace.reporting.endpoint,
                'secure': self.hypertrace.reporting.secure,
                'trace_reporter_type': traceable_hypertrace_config.TraceReporterType.Name(self.hypertrace.reporting.trace_reporter_type), # pylint:disable=C0301
            },
            'data_capture': {
                'http_headers': {
                    'request': self.hypertrace.data_capture.http_headers.request.value,
                    'response': self.hypertrace.data_capture.http_headers.response.value,
                },
                'http_body': {
                    'request': self.hypertrace.data_capture.http_body.request.value,
                    'response': self.hypertrace.data_capture.http_body.response.value,
                },
                'rpc_metadata': {
                    'request': self.hypertrace.data_capture.rpc_metadata.request.value,
                    'response': self.hypertrace.data_capture.rpc_metadata.response.value,
                },
                'rpc_body': {
                    'request': self.hypertrace.data_capture.rpc_body.request.value,
                    'response': self.hypertrace.data_capture.rpc_metadata.response.value,
                },
                'body_max_size_bytes': self.hypertrace.data_capture.body_max_size_bytes,
            },
            'opa': {
                'enabled': self.traceable.opa.enabled.value,
                'endpoint': self.traceable.opa.endpoint.value,
                'poll_period_seconds': self.traceable.opa.poll_period_seconds.value
            },
            'blocking_config': {
                'enabled': self.traceable.blocking_config.enabled.value,
                'debug_log': self.traceable.blocking_config.debug_log.value,
                'evaluate_body': self.traceable.blocking_config.evaluate_body.value,
                'modsecurity': {
                    'enabled': self.traceable.blocking_config.modsecurity.enabled.value,
                },
                'skip_internal_request': self.traceable.blocking_config.skip_internal_request.value,
                'region_blocking': {
                    'enabled': self.traceable.blocking_config.region_blocking.enabled.value,
                },
                'remote_config': {
                    'enabled': self.traceable.blocking_config.remote_config.enabled.value,
                    'endpoint': self.traceable.blocking_config.remote_config.endpoint.value,
                    'poll_period_seconds': self.traceable.blocking_config.remote_config.poll_period_seconds.value,
                }
            }
        }
