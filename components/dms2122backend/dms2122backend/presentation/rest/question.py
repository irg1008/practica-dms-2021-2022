from typing import Dict, Optional, Tuple

from flask.globals import current_app

from dms2122backend.service.auth.protected_endpoint_dec import protected_endpoint
from dms2122common.data.role import Role


@protected_endpoint(roles=[Role.Teacher])
def new(body: Dict, token_info: Dict = {}, **kwargs) -> Tuple[str, Optional[int]]:
    """New question endpoint

    Roles: Teacher

    Returns:
        Tuple[str, Optional[int]]: Response message and status code
    """
    print(body, flush=True)
    print(token_info, flush=True)

    return ("", 200)


def getQ():
    pass


def editQ():
    pass


def getAll():
    pass
