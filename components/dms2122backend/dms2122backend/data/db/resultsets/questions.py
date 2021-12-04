from typing import List

from dms2122backend.data.db.results.question import Question
from sqlalchemy.orm.session import Session  # type: ignore


class Questions:
    @staticmethod
    def list_all(session: Session) -> List[Question]:
        try:
            questions = session.query(Question).all()
            session.commit()

            return questions
        except Exception:
            session.rollback()
            return []
