from typing import Union
from flask import g
from dms2122frontend.data.config.frontendconfiguration import FrontendConfiguration
from dms2122frontend.data.rest.backendservice import BackendService
from dms2122frontend.data.rest.database_client.restDB import RestDB
from dms2122frontend.data.rest.database_client.mockDB import mockDB
from dms2122frontend.data.rest.database_client.database_client import DatabaseClient

__db = None


def get_db() -> DatabaseClient:
    """Returns an aplication context database instance

    Returns:
        Database: Current application database adapter
    """
    global __db

    if __db is None:
        service = get_backend_service()
        __db = RestDB(
            service.get_base_url(),
            service.get_apikey_secret(),
            service.get_apikey_header(),
        )

    return __db


def teardow_db():
    """
    Destroys the current DB object
    """
    db = g.pop("db", None)

    if db is not None:
        del db


__backendService: Union[BackendService, None] = None


def get_backend_service() -> BackendService:
    global __backendService
    if __backendService is None:
        raise Exception("You have not set the backend service")

    return __backendService


def set_backend_service(service: BackendService) -> None:
    global __backendService
    __backendService = service
