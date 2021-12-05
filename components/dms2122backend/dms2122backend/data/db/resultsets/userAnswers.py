from typing import List

from dms2122backend.data.db.results.question import Question  # type: ignore
from dms2122backend.data.db.results.answeredQuestion import AnsweredQuestion  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore


class UserAnswers:
    @staticmethod
    def get_aswered(session: Session, username: str) -> List[Question]:
        """Retrieves the user answered questions

        Args:
            session (Session): Current Working Session
            username (str): User ID

        Raises:

        Returns:
            List[Question]: User's Answered Questions
        """
        _answered_questions: List[AnsweredQuestion] = session.query(
            AnsweredQuestion).filter_by(iduser=username).all()

        answered_questions: List[Question] = session.query(
            Question).join(_answered_questions).all()

        return answered_questions

    @staticmethod
    def get_unaswered(session: Session, username: str) -> List[Question]:
        """Retrieves the user unanswered questions

        Args:
            session (Session): Current Working Session
            username (str): User ID

        Raises:

        Returns:
            List[Question]: User's Unanswered Questions
        """
        answered_questions: List[Question] = UserAnswers.get_aswered(
            session, username)

        all_questions: List[Question] = session.query(Question).all()

        unanswered_questions: List[Question] = [
            q for q in all_questions if q not in answered_questions]

        return unanswered_questions
