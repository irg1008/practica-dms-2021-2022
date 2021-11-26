from sqlalchemy import Table, MetaData, Column, String  # type: ignore
from sqlalchemy.orm import mapper, relationship  # type: ignore
from .answeredQuestion import AnsweredQuestion


class User():
    def __init__(self, username: str, password: str):
        self.username: str = username
        self.password: str = password
        # self.salt: str = salt # TODO: fijar salt

    @classmethod
    def map(cls: type, metadata: MetaData) -> None:
        mapper(
            cls,
            Table(
                'users',
                metadata,
                Column('username', String(32), primary_key=True),
                Column('password', String(64), nullable=False)
                #Column('salt', String(64), nullable=False) # TODO: fijar salt
            ),
            properties={
                'sessions': relationship(AnsweredQuestion, backref='answeredQuestions')
            }
        )