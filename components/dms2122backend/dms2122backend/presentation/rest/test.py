from http import HTTPStatus
from typing import Dict, List

from flask.globals import current_app
from dms2122backend.data.db.results.question import Question
from dms2122backend.data.db.resultsets.dbmanager import DBManager
from dms2122backend.data.db.schema import Schema  # type: ignore


def test(body: Dict, **kwargs):

    print(body, flush=True)
    question_title = kwargs.get("title")
    with current_app.app_context():
        db: Schema = current_app.db

