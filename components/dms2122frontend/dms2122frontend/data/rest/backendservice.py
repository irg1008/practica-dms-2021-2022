""" BackendService class module.
"""

import requests
from dms2122common.data import Role
from dms2122common.data.rest import ResponseData


class BackendService:
    """ REST client to connect to the backend service.
    """

    def __init__(
        self,
        host: str,
        port: int,
        api_base_path: str = "/api/v1",
        apikey_header: str = "X-ApiKey-Backend",
        apikey_secret: str = "",
    ):
        """ Constructor method.

        Initializes the client.

        Args:
            - host (str): The backend service host string.
            - port (int): The backend service port number.
            - api_base_path (str): The base path that is prepended to every request's path.
            - apikey_header (str): Name of the header with the API key that identifies this client.
            - apikey_secret (str): The API key that identifies this client.
        """
        self.__host: str = host
        self.__port: int = port
        self.__api_base_path: str = api_base_path
        self.__apikey_header: str = apikey_header
        self.__apikey_secret: str = apikey_secret

    def __base_url(self) -> str:
        return f"http://{self.__host}:{self.__port}{self.__api_base_path}"

    def get_base_url(self) -> str:
        """Gets the formated base url

        Returns:
            str: formated base url
        """
        return self.__base_url()

    def get_apikey_header(self) -> str:
        """ Gets backend the api key header

        Returns:
            str: api key header
        """
        return self.__apikey_header

    def get_apikey_secret(self) -> str:
        """Gets the backend api key secret

        Returns:
            str: api key secret
        """
        return self.__apikey_secret
