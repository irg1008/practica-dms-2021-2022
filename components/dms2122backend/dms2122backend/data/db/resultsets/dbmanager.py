from typing import Any, Generic, List, TypeVar

from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.sql.schema import Table  # type: ignore
from dms2122backend.data.db.results.resultbase import ResultBase


T = TypeVar("T")


class DBManager(Generic[T]):
    @staticmethod
    def create(session: Session, row) -> bool:
        """ Adds a new row to his table

        Args:
            session (Session): Working Session
            row (): object to add

        Returns:
            bool: True if added successfully
        """
        session.begin()
        try:
            session.add(row)
        except:
            session.rollback()
            return False
        else:
            session.commit()
            return True

    @staticmethod
    def list_all(session: Session, table: Any) -> List[Any]:
        return session.query(table).all()

    @staticmethod
    def select_by(table: Any, session: Session, **attributes) -> List:
        return session.query(table).filter_by(**attributes).all()

    @staticmethod
    def edit(session: Session, id: int, updated: Any) -> int:
        """Edits an existing question, throws an exception if the question does not exist.

        Args:
            session (Session): Working Session
            id (int): Question Id

        Returns:
            int: Question ID
        """
        raise NotImplemented

