""" WebAuth class module.
"""

from typing import List
from flask import session
from dms2122common.data.rest import ResponseData, responsedata
from dms2122backend.service.auth._authservice import AuthService
from dms2122common.data.role import Role


class BackAuth:
    """ Monostate class responsible of the authentication operation utilities.
    """

    @staticmethod
    def has_role(
        auth_service: AuthService, token: str, username: str, roles: List[Role]
    ) -> bool:
        """Checks if a user has any of the roles

        Args:
            auth_service (AuthService): [description]
            roles (Role[]): List of roles to check

        Returns:
            bool: [description]
        """

        response = auth_service.get_user_roles(token, username)

        if not response.is_successful:
            return False

        if response.get_content() is None or not isinstance(
            response.get_content(), list
        ):
            return False
        role_list = list(response.get_content())

        for rol in roles:
            if rol.value in role_list:
                return True
        return False
