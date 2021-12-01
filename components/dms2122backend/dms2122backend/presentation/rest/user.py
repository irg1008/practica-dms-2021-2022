from typing import Dict, Optional, Tuple

from flask.globals import current_app

from dms2122backend.service.auth.protected_endpoint_dec import protected_endpoint
from dms2122common.data.role import Role


@protected_endpoint(roles=[Role.Teacher, Role.Student])
def get_unanswered_questions(body: Dict, **kwargs) -> Tuple[int, Optional[int]]:
    """Get user unanswered questions.

    Roles: Teacher and Specific Student

    Returns:
        Tuple[str, Optional[int]]: Response message and status code
    """

    return (1, 200)

@protected_endpoint(roles=[Role.Teacher, Role.Student])
def get_answered_questions(body: Dict, **kwargs) -> Tuple[int, Optional[int]]:
    """Get user answered questions.

    Roles: Teacher and Specific Student

    Returns:
        Tuple[str, Optional[int]]: Response message and status code
    """

    return (1, 200)
  
@protected_endpoint(roles=[Role.Teacher, Role.Student])
def get_question_answer(body: Dict, **kwargs) -> Tuple[int, Optional[int]]:
    """Get the answer for a user on an especific question.

    Roles: Teacher and Specific Student

    Returns:
        Tuple[str, Optional[int]]: Response message and status code
    """

    return (1, 200)

@protected_endpoint(roles=[Role.Student])
def post_question_answer(body: Dict, **kwargs) -> Tuple[int, Optional[int]]:
    """Sets the answer for a user on an especific question.

    Roles: Teacher and Specific Student

    Returns:
        Tuple[str, Optional[int]]: Response message and status code
    """

    return (1, 200)