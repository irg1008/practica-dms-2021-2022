from typing import Optional, Tuple, Dict, Union
from dms2122backend.service.auth.protected_endpoint_dec import protected_endpoint
from http import HTTPStatus
from dms2122common.data.role import Role


@protected_endpoint(roles=[Role.Teacher, Role.Student])
def get_stats(username: str, **kwargs) -> Tuple[str, Optional[int]]:
    """Get the stats for a specific user.

    Returns:
        - Tuple[None, Optional[int]]: A tuple of no content and code 204 No Content.
    """

    return (f"Getting stats for user {username}", HTTPStatus.ACCEPTED.value)


def update_stats(body: Dict, token_info: Dict) -> Tuple[Union[Dict, str], Optional[int]]:
    """Update the stats for the user.

    Returns:
        - Tuple[None, Optional[int]]: A tuple of no content and code 204 No Content.
    """
    return ("Getting stats", HTTPStatus.OK.value)
