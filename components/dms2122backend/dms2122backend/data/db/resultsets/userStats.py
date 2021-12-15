from typing import List
from dms2122backend.data.db.results.userStats import UserStats as UserResults  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from dms2122backend.data.db.resultsets.dbmanager import DBManager


class UserStats:
    @staticmethod
    def get_stats(session: Session, iduser: str):
        """Retrieves the user stats

        Args:
            session (Session): Current Working Session
            iduser (str): User ID
            idquestion (str): Question ID

        Raises:

        Returns:
            AnsweredQuestion: User's answer to a certain question
        """
        session.begin()
        try:
            stats: UserResults = DBManager.first(UserResults, session, iduser=iduser)
        except:
            session.rollback()
            return None
        else:
            session.commit()
            return stats

    @staticmethod
    def get_all_users_stats(session: Session):
        """Retrieves the user stats

        Args:
            session (Session): Current Working Session
            iduser (str): User ID
            idquestion (str): Question ID

        Raises:

        Returns:
            AnsweredQuestion: User's answer to a certain question
        """
        session.begin()
        try:
            stats: List[UserResults] = DBManager.list_all(session, UserResults)
        except:
            session.rollback()
            return None
        else:
            session.commit()
            return stats
