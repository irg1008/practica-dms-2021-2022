from sqlalchemy import Table, MetaData, Column, String, Integer, DateTime  # type: ignore
from sqlalchemy.orm import mapper, relationship  # type: ignore
from datetime import datetime

from sqlalchemy.sql.schema import ForeignKey

class AnsweredQuestion():
    def __init__(self, idquestion: int, iduser: str, answer: str):
        self.idquestion: int = idquestion
        self.iduser: str = iduser
        self.answer: int = answer
        self.score: float = 0
        self.date = datetime.now()

    @classmethod
    def map(cls: type, metadata: MetaData) -> None:
        mapper(
            cls,
            Table(
                'answeredQuestions',
                metadata,
                Column('idquestion', Integer, ForeignKey('questions.id'), 
                       primary_key=True),
                Column('iduser', String(32), ForeignKey('users.id'),
                       primary_key=True),
                Column('answer', String(250), nullable=False),
                Column('date', DateTime, nullable=False)
            )
        )