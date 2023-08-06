import os
import traceback
from contextlib import contextmanager

import distro

# These imports have to be first to respect TA_ env vars in hypertrace agent
from hypertrace import env_var_settings

from traceableai.config.config import Config
from traceableai.config_wrapper import ConfigWrapper
from traceableai.hypertrace_env_override import add_deprecation_to_ht_env

env_var_settings.ENV_VAR_PREFIXES.insert(0, 'TA')
add_deprecation_to_ht_env()

from hypertrace import agent  # pylint:disable=C0413,C0411,C0412
from hypertrace.agent.filter.registry import Registry # pylint:disable=C0413,C0411,C0412
from hypertrace.agent.custom_logger import get_custom_logger # pylint:disable=C0413,C0411,C0412
from hypertrace.agent import constants # pylint:disable=C0413,C0411,C0412

from traceableai.version import __version__ # pylint:disable=C0413

logger = get_custom_logger(__name__)


# We need to override the version that is reported to the platform from hypertrace
constants.TELEMETRY_SDK_VERSION = __version__

class Agent(agent.Agent):
    def __init__(self):
        super().__init__()
        self.is_lambda = False
        logger.debug("Platform: %s", distro.id())
        logger.debug("Platform version: %s", distro.version())
        logger.debug('TraceableAI Agent version: %s', __version__)
        logger.debug("successfully initialized traceableai agent")

        if hasattr(os, 'register_at_fork'):
            logger.info('Registering after_in_child handler.')
            os.register_at_fork(after_in_child=self.post_fork)  # pylint:disable=E1101

    def post_fork(self):
        logger.info("In post fork hook")
        logger.info("Calling add traceable filter during post fork")
        self._init.post_fork()
        self.add_traceable_filter()

    @contextmanager
    def edit_config(self):
        """Used by end users to modify the config"""
        with super().edit_config() as ht_config:
            bundled_config = ConfigWrapper(ht_config, Config().config)
            config_dict = bundled_config.current_config()
            yield config_dict
            bundled_config.apply_modifications(config_dict)


    def add_traceable_filter(self):  #pylint:disable=R0201
        logger.debug("in add_traceable_filter")
        if self.is_lambda:
            logger.info('Not loading blocking extension - currently unsupported in lambda')
            return
        # We need to do a local import so that the extension is not loaded in a parent process
        from traceableai.filter.traceable import Traceable, _LIBTRACEABLE_AVAILABLE  # pylint:disable=C0413,C0412,C0415
        if not _LIBTRACEABLE_AVAILABLE:
            logger.info("libtraceable unavailable, skipping filter registration")
            return
        if Config().config.blocking_config.enabled.value is not True:
            logger.info("Not adding libtraceable filter - blocking is not enabled")
            return
        try:
            Registry().register(Traceable)
            logger.debug("successfully initialized traceable filter")
        except Exception as exc: # pylint:disable=W0703
            logger.debug(''.join(traceback.format_exception(None, exc, exc.__traceback__)))
            logger.info("failed to register traceable filter")
