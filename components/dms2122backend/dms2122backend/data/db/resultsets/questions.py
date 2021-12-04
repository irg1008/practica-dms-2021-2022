from typing import List

from dms2122backend.data.db.results.question import Question
from sqlalchemy.orm.session import Session  # type: ignore


class Questions:
    @staticmethod
    def create(session: Session, question: Question) -> int:
        """ Creates a new question

        Args:
            session (Session): Working Session
            question (Question): Question to persist        
        Raises:
            QuestionAlreadyExists

        Returns:
            int: Question Id
        """
        raise NotImplemented

    @staticmethod
    def list_all(session: Session) -> List[Question]:
        try:
            questions = session.query(Question).all()
            session.commit()

            return questions
        except Exception:
            session.rollback()
            return []

    @staticmethod
    def get_by_id(session: Session, id: int) -> Question:
        raise NotImplemented

    @staticmethod
    def edit(session: Session, id: int, updated: Question) -> int:
        """Edits an existing question, throws an exception if the question does not exist.

        Args:
            session (Session): Working Session
            id (int): Question Id
            

        Raises:


        Returns:
            int: Question ID
        """
        raise NotImplemented

