from typing import List

from sqlalchemy.orm.session import Session  # type: ignore

class DBManager:
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
    def remove(session: Session, row) -> bool:
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
    def list_all(session: Session, table) -> List:
        return session.query(table).all()

    @staticmethod
    def select_by(table, session: Session, **attributes) -> List:
        return session.query(table).filter_by(attributes).all()

