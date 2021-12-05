from typing import Any, Generic, List, TypeVar, Union

from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.sql.schema import Table  # type: ignore
from dms2122backend.data.db.results.resultbase import ResultBase


T = TypeVar("T")


class DBManager(Generic[T]):
    @staticmethod
    def create(session: Session, row: T) -> Union[T, None]:
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
            return None
        else:
            session.commit()
            return row

    @staticmethod
    def remove(session: Session, row: T) -> bool:
        session.begin()
        try:
            session.delete(row)
        except:
            session.rollback()
            return False
        else:
            session.commit()
            return True

    @staticmethod
    def list_all(session: Session, table: T) -> List:
        return session.query(table).all()

    @staticmethod
    def row_exists(table, session: Session, **attributes) -> bool:
        """ Determines if exists any row with the attributes given

            Args:
                - session (Session): The session object.
                - **attributes: attributes for the filter

            Returns:
                - bool: `True` if exists.
            """
        try:
            query = session.query(table).filter_by(**attributes)
            query.one()
        except:
            return False
        return True

    @staticmethod
    def select_by(table, session: Session, **attributes) -> List:
        return session.query(table).filter_by(**attributes).all()
