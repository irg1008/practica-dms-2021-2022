from typing import Dict, Optional, Tuple

from flask.globals import current_app

from dms2122backend.service.auth.protected_endpoint_dec import protected_endpoint
from dms2122common.data.role import Role


@protected_endpoint(roles=[Role.Teacher])
def new(body: Dict, **kwargs) -> Tuple[int, Optional[int]]:
    """New question endpoint

    Roles: Teacher

    Returns:
        Tuple[int, Optional[int]]: if 200 - Question ID and status code
    """

    body
    return (1, 200)


@protected_endpoint(roles=[Role.Teacher, Role.Student])
def getQ(id: int, **kwargs):
    return ({"id": id}, 200)


@protected_endpoint(roles=[Role.Teacher])
def editQ(id: int, **kwargs):
    return (id, 200)


def getAll(**kwargs):
    return ({}, 200)
