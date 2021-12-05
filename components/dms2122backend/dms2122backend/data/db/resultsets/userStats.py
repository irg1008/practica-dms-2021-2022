from typing import List
from dms2122backend.data.db.results.question import Question  # type: ignore
from dms2122backend.data.db.results.answeredQuestion import AnsweredQuestion  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from dbmanager import DBManager


class UserStats:

