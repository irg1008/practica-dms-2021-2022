from typing import Any, Callable, Dict, List, Optional, Tuple, TypeVar, Union
from http import HTTPStatus
from flask.globals import current_app
from dms2122common.data.role import Role
from dms2122backend.service.auth._authservice import AuthService
from dms2122backend.service.auth.backauth import BackAuth
from dms2122backend.g import get_auth_service

F = TypeVar("F", bound=Callable[..., Any])

# https://stackoverflow.com/a/26151604/11810358
def parametrized(dec):
    """Decorator that adds parameters to a decorator

    Args:
        dec (Callable): A decorator
    """

    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)

        return repl

    return layer


@parametrized
def protected_endpoint(
    route_fun: Callable[..., Tuple[Any, Optional[int]]] = None, roles: List[Role] = []
) -> Callable[..., Tuple[Any, Optional[int]]]:
    """Decorator that validates a Token and asserts that the user has any of the roles.

    If the Role List is empty, there is no role check

    Args:
        route_fun (Callable[..., Tuple[str, Optional[int]]], optional): A function to decorate. Defaults to None.
        roles (List[Role], optional): A List of roles returns 403 if the user has no role. Defaults to [].

    Raises:
        Exception: If not used as a decorator

    Returns:
        Callable[..., Tuple[str, Optional[int]]]: A function to call that returns an HTTP Status and Message
    """

    # with current_app.app_context():

    # auth_service: AuthService = current_app.auth_servic
    auth_service = get_auth_service()

    def route_aux(*args, **kwargs) -> Tuple[Any, Optional[int]]:
        if route_fun is None:
            raise Exception("This is a decorator, not a normal function!")

        if not "token_info" in kwargs:
            return "No info was parsed from headers", None

        headers: Union[Dict, None] = kwargs.get("token_info")

        if not headers or not headers.get("user_token"):
            return ("User Token is Invalid", 400)

        user_token: Union[Dict, None] = headers.get("user_token")

        if not user_token:
            return ("User Token is Invalid", 400)

        token = user_token.get("auth_token")
        username = user_token.get("user")

        if not BackAuth.has_role(auth_service, token or "", username or "", roles):
            return (
                "You don't have enough permission to do this action",
                HTTPStatus.FORBIDDEN,
            )

        return route_fun(*args, **kwargs)

    return route_aux

