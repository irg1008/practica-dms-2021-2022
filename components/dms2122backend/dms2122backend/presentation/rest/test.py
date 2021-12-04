from http import HTTPStatus
from typing import Dict

from flask.globals import current_app
from dms2122backend.data.db.resultsets.questions import Questions
from dms2122backend.data.db.schema import Schema  # type: ignore


def test(body: Dict, **kwargs):

    print(body, flush=True)
    question_title = kwargs.get("title")
    with current_app.app_context():
        db: Schema = current_app.db
        s = db.new_session()
        return [q.to_JSON() for q in Questions.list_all(s)], HTTPStatus.OK
