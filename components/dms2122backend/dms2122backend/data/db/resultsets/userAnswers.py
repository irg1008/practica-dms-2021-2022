from typing import List

from dms2122backend.data.db.results.question import Question
from sqlalchemy.orm.session import Session  # type: ignore


class UserAnswers:
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
        raise NotImplemented
