from components.dms2122auth.dms2122auth.data.db.results.user import User
from dms2122backend.data.db.results.question import Question  # type: ignore
from dms2122backend.data.db.results.userStats import UserStats  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from dbmanager import DBManager


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
            stats: UserStats = DBManager.first(
                UserStats, session, iduser=iduser)
        except:
            session.rollback()
            return None
        else:
            session.commit()
            return stats
