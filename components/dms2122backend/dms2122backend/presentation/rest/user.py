import json
from typing import Dict, Optional, Tuple, Union, List
from http import HTTPStatus
from dms2122backend.data.db.schema import Schema  # type: ignore
from flask.globals import current_app
from dms2122backend.data.db.resultsets.questions import Questions
from dms2122backend.service.auth.protected_endpoint_dec import protected_endpoint
from dms2122common.data.role import Role


@protected_endpoint(roles=[Role.Teacher, Role.Student])
def get_unanswered_questions(
    username: str, **kwargs
) -> Tuple[Union[List[Dict], str], int]:
    with current_app.app_context():
        db: Schema = current_app.db
        s = db.new_session()

        uns_ques = Questions.get_unanswered(s, username)

        if len(uns_ques) == 0:
            return "No unanswered questions", HTTPStatus.NOT_FOUND

        return [q.to_JSON() for q in uns_ques], HTTPStatus.OK


@protected_endpoint(roles=[Role.Teacher, Role.Student])
def get_answered_questions(
    username: str, **kwargs
) -> Tuple[Union[List[Dict], str], int]:
    with current_app.app_context():
        db: Schema = current_app.db
        s = db.new_session()

        question, ans_ques = Questions.get_answered(s, username)

        if len(ans_ques) == 0:
            return "No answered questions", HTTPStatus.NOT_FOUND

        # Add question json to answered question.
        ans_dict_list = []
        for q, a in zip(question, ans_ques):
            a_dict = a.to_JSON()
            a_dict["question"] = q.to_JSON()

        return ans_dict_list, HTTPStatus.OK


# @protected_endpoint(roles=[Role.Student])
def post_question_answer(
    username: str, id: int, body: Dict, **kwargs
) -> Tuple[str, Optional[int]]:
    """Sets the answer for a user on an especific question.

    Roles: Teacher and Specific Student

    Returns:
        Tuple[str, Optional[int]]: Response message and status code
    """
    with current_app.app_context():
        db: Schema = current_app.db
        s = db.new_session()
        ans = body.get("answer")

        if not ans:
            return ("There is no answer", HTTPStatus.BAD_REQUEST)

        res = Questions.set_user_question_answer(s, id, username, ans)

        if not res:
            return (
                "There was an error while answering the question",
                HTTPStatus.BAD_REQUEST,
            )

        return ("Question Answered", HTTPStatus.ACCEPTED)
