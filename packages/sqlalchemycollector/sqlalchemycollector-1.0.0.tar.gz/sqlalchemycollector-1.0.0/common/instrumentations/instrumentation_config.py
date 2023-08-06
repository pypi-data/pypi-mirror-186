import os
from urllib.parse import urlparse
from distutils.util import strtobool

from .consts import METIS_DISABLED_ENV_VAR_STR, \
    METIS_SERVICE_NAME_ENV_VAR_STR, \
    METIS_EXPORTER_ENV_VAR_STR, \
    METIS_API_KEY_ENV_VAR_STR, \
    METIS_SERVICE_VERSION_ENV_VAR_STR


def is_valid_url(url):
    try:
        result = urlparse(url)
        return all(['http' in result.scheme, 'metisdata' in result.path])
    except ValueError:
        return False


class InstrumentationEnvConfig:
    def __init__(self, service_name, exporter_url, api_key, service_version=None):
        self.service_name = service_name
        self.service_version = service_version
        self.exporter_url = exporter_url
        self.api_key = api_key
        self.is_disabled = strtobool(os.getenv(METIS_DISABLED_ENV_VAR_STR, "0"))

        os.environ['OTEL_PYTHON_DISABLE_INSTRUMENTATION'] = str(self.is_disabled)
        os.environ['OTEL_SDK_DISABLED'] = str(self.is_disabled)

        self._extract_from_env()

    @staticmethod
    def create(user_conf: dict):
        return InstrumentationEnvConfig(user_conf['service_name'],
                                        user_conf['service_version'],
                                        user_conf['exporter_url'],
                                        user_conf['api_key'])

    def _extract_from_env(self):
        service_name = os.getenv(METIS_SERVICE_NAME_ENV_VAR_STR)
        if service_name:
            self.service_name = service_name

        service_version = os.getenv(METIS_SERVICE_VERSION_ENV_VAR_STR)
        if service_version:
            self.service_name = service_version

        api_key = os.getenv(METIS_API_KEY_ENV_VAR_STR)
        if api_key:
            self.api_key = api_key

        exporter_url = os.getenv(METIS_EXPORTER_ENV_VAR_STR)
        if exporter_url:
            self.exporter_url = exporter_url
