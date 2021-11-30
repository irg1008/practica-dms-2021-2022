from typing import Dict
from dms2122backend.data.config.backendconfiguration import BackendConfiguration
from dms2122backend.service.auth._authservice import AuthService

__auth_service = None


def get_auth_service() -> AuthService:
    global __auth_service
    if __auth_service is None:
        cfg: BackendConfiguration = BackendConfiguration()
        auth_service_cfg: Dict = cfg.get_auth_service()
        __auth_service = AuthService(
            auth_service_cfg["host"],
            auth_service_cfg["port"],
            apikey_header="X-ApiKey-Auth",
            apikey_secret=auth_service_cfg["apikey_secret"],
        )

    return __auth_service
