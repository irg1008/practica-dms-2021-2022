from sqlalchemy import Table, MetaData, Column, String, Integer, Float, Boolean  # type: ignore
from sqlalchemy.orm import mapper, relationship  # type: ignore
from .answeredQuestion import AnsweredQuestion


class Question():
    def __init__(self, title: str, statement: str, correctOption: str, 
                 score: float=0, penalty: float=0, public: bool=True):
        #self.id: int = #generador de ids
        self.title: str = title
        self.statement: str = statement
        self.correctOption: str = correctOption
        #self.incorrectOptions: list[str] = incorrectOptions
        self.score: float = score
        self.penalty: float = penalty
        self.public: bool = public
        self.ncorrect: int = 0
        self.nanswered: int = 0

    @classmethod
    def map(cls: type, metadata: MetaData) -> None:
        mapper(
            cls,
            Table(
                'questions',
                metadata,
                Column('id', Integer, primary_key=True),
                Column('title', String(250), nullable=False),
                Column('statement', String(250), nullable=False),
                Column('correctOption', String(250), nullable=False),
                #Column('incorrectOptions', json, nullable=False), # TODO: hacer json
                Column('score', Float, default=0),
                Column('penalty', Float, default=0),
                Column('public', Boolean, default=True),
                Column('ncorrect', Integer, default=0),
                Column('nanswered', Integer, default=0)
            ),
            properties={
                'sessions': relationship(AnsweredQuestion, backref='answeredQuestions')
            }
        )