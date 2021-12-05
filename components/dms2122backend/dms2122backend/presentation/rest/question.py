from typing import Dict, List, Optional, Tuple, Union
from http import HTTPStatus
from flask.globals import current_app
from dms2122backend.data.db.resultsets.questions import Questions
from dms2122backend.data.db.results.question import Question
from dms2122backend.data.db.resultsets.dbmanager import DBManager
from dms2122backend.data.db.schema import Schema  # type: ignore


from dms2122backend.service.auth.protected_endpoint_dec import protected_endpoint
from dms2122common.data.role import Role


@protected_endpoint(roles=[Role.Teacher])
def new(body: Dict, **kwargs) -> Tuple[Union[str, int], Optional[int]]:
    """New question endpoint

    Roles: Teacher

    Returns:
        Tuple[str, Optional[int]]: Response message and status code
    """
    print(body, flush=True)
    with current_app.app_context():
        db: Schema = current_app.db
        question = Question.From_Json(body)
        res = DBManager.create(db.new_session(), question)

        if not res:
            return (
                "There was an error while creating the question",
                HTTPStatus.BAD_REQUEST,
            )

        return res.id, HTTPStatus.ACCEPTED


@protected_endpoint(roles=[Role.Teacher, Role.Student])
def getQ(id: int, **kwargs):
    try:
        with current_app.app_context():
            db: Schema = current_app.db
            session = db.new_session()

            res: List[Question] = DBManager.select_by(Question, session, id=id)
            return res[0].to_JSON(), HTTPStatus.ACCEPTED
    except Exception:
        return "The question does not exist", HTTPStatus.BAD_REQUEST


@protected_endpoint(roles=[Role.Teacher])
def editQ(id: int, body: Dict, **kwargs):
    with current_app.app_context():
        db: Schema = current_app.db
        question = Question.From_Json(body)
        res = Questions.editQuestion(db.new_session(), id, question)

        if res:
            return "Question Edited", HTTPStatus.OK
        else:
            return "The question could not be edited", HTTPStatus.BAD_REQUEST


@protected_endpoint(roles=[Role.Teacher])
def getAll(**kwargs):

    with current_app.app_context():
        db: Schema = current_app.db
        s = db.new_session()
        res: List[Question] = DBManager.list_all(s, Question)
        return [q.to_JSON() for q in res], HTTPStatus.OK

