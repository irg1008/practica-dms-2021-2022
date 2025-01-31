
""" AnsweredQuestion class module.
"""
from typing import Dict
from sqlalchemy import Table, MetaData, Column, ForeignKey, String, DateTime, Integer # type: ignore
from dms2122backend.data.db.results.resultbase import ResultBase # type: ignore
from datetime import datetime


class AnsweredQuestion(ResultBase):
    """ Definition and storage of the answered questions.
    """

    def __init__(self, idquestion: int, iduser: str, answer: str):
        """ Constructor method.

        Initializes a answeredQuestion role record.

        Args:
            - idquestion (str): Title of the referenced question.
            - iduser (str): Name of the user owner
            - answer (str): String of the answer
            - date (datetime): Date if the creation 
        """
        self.idquestion: int = idquestion
        self.iduser: str = iduser
        self.answer: str = answer
        self.date = datetime.now()

    @staticmethod
    def _table_definition(metadata: MetaData) -> Table:
        """ Gets the table definition.

        Args:
            - metadata (MetaData): The database schema metadata
                        (used to gather the entities' definitions and mapping)

        Returns:
            - Table: A `Table` object with the table definition.
        """
        return Table(
            'answered_questions',
            metadata,
            Column('idquestion', Integer, ForeignKey('questions.id'),
                   primary_key=True),
            # ForeignKey('Users.username'),
            Column('iduser', String(32), primary_key=True),
            Column('answer', String(250), nullable=False),
            Column('date', DateTime, nullable=False)
        )

    def to_JSON(self,) -> Dict:
        d = {
            "answer": self.answer,
            "date": self.date.timestamp(),
        }
        return d
