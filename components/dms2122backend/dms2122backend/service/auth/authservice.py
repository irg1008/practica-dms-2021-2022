""" AuthService class module.
"""

from typing import List, Optional, Union
import requests
from dms2122common.data import Role
from dms2122common.data.rest import ResponseData


class AuthService:
    """ REST client to connect to the authentication service.
    """

    def __init__(
        self,
        host: str,
        port: int,
        api_base_path: str = "/api/v1",
        apikey_header: str = "X-ApiKey-Auth",
        apikey_secret: str = "",
    ):
        """ Constructor method.

        Initializes the client.

        Args:
            - host (str): The authentication service host string.
            - port (int): The authentication service port number.
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
        """ Constructs the base URL for the requests.

        Returns:
            - str: The base URL.
        """
        return f"http://{self.__host}:{self.__port}{self.__api_base_path}"

    def get_user_roles(self, token: Optional[str], username: str) -> ResponseData:
        """ Requests the list of roles assigned to a user.

        Args:
            - token (Optional[str]): The user session token.
            - username (str): The name of the queried user.

        Returns:
            - ResponseData: If successful, the contents hold a list of role names. Otherwise an
              empty list.
        """
        response_data: ResponseData = ResponseData()
        response: requests.Response = requests.get(
            self.__base_url() + f"/user/{username}/roles",
            headers={
                "Authorization": f"Bearer {token}",
                self.__apikey_header: self.__apikey_secret,
            },
        )
        response_data.set_successful(response.ok)
        if response_data.is_successful():
            response_data.set_content(response.json())
        else:
            response_data.add_message(response.content.decode("ascii"))
            response_data.set_content([])
        return response_data
