from typing import Dict, Optional, Tuple
from http import HTTPStatus
from flask.globals import current_app

from dms2122backend.service.auth.protected_endpoint_dec import protected_endpoint
from dms2122common.data.role import Role


@protected_endpoint(roles=[Role.Teacher])
def new(body: Dict, **kwargs) -> Tuple[int, Optional[int]]:
    """New question endpoint

    Roles: Teacher

    Returns:
        Tuple[str, Optional[int]]: Response message and status code
    """

    return (1, HTTPStatus.OK)


@protected_endpoint(roles=[Role.Teacher, Role.Student])
def getQ(id: int, **kwargs):
    return (
        {
            "id": 1,
            "statement": 2,
            "title": "Hehehehe",
            "correct_answer": "HOla",
            "incorrect_answers": ["Ha", "He", "Hi"],
            "score": 10,
            "penalty": 50,
            "image_url": "https://pbs.twimg.com/media/FFpEinEXEAIh76B?format=jpg&name=medium",
            "public": True,
            "user_answers": {"Ha": 5, "He": 5, "Hi": 0, "HOla": 200},
        },
        200,
    )


@protected_endpoint(roles=[Role.Teacher])
def editQ(id: int, **kwargs):
    return (id, HTTPStatus.OK)


@protected_endpoint(roles=[Role.Teacher])
def getAll(**kwargs):

    questions = [
        {
            "id": 1,
            "statement": 2,
            "title": "Hehehehe",
            "correct_answer": "HOla",
            "incorrect_answers": ["Ha", "He", "Hi"],
            "score": 10,
            "penalty": 50,
            "image_url": "https://pbs.twimg.com/media/FFpEinEXEAIh76B?format=jpg&name=medium",
            "public": True,
            "user_answers": {"Ha": 5, "He": 5, "Hi": 0, "HOla": 200},
        }
    ]

    return (questions, HTTPStatus.OK)
