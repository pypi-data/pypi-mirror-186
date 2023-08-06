import os

from hypertrace import env_var_settings
from hypertrace.agent.custom_logger import get_custom_logger # pylint:disable=C0413,C0411,C0412
logger = get_custom_logger(__name__)

def ta_get_env_value(target_key):
    for prefix in env_var_settings.ENV_VAR_PREFIXES:
        env_var_key = f"{prefix}_{target_key}"
        if env_var_key in os.environ:
            if env_var_key.startswith('HT_'):
                logger.warning("[Deprecated] - HT_ prefixed environment "
                               "variables should be updated to instead be prefixed with TA_")
                logger.warning("[Deprecated] - Update from %s to TA_%s", env_var_key, target_key)
            return os.environ[env_var_key]
    return None


def add_deprecation_to_ht_env():
    env_var_settings.get_env_value = ta_get_env_value
