
""" AnsweredQuestion class module.
"""

from sqlalchemy import Table, MetaData, Column, ForeignKey, String, DateTime, Integer  # type: ignore
from dms2122backend.data.db.results.resultbase import ResultBase
from datetime import datetime


class AnsweredQuestion(ResultBase):
    """ Definition and storage of the answered questions.
    """

    def __init__(self, idquestion: int, iduser: str, answer: int):
        """ Constructor method.

        Initializes a answeredQuestion role record.

        Args:
            - idquestion (str): Title of the referenced question.
            - iduser (str): Name of the user owner
            - answer (str): String of the answer
            - score (float): Score
            - date (datetime): Date if the creation 
        """
        self.idquestion: int = idquestion
        self.iduser: str = iduser
        self.answer: int = answer
        self.score: float = 0
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
            Column('iduser', String(32), primary_key=True), # ForeignKey('Users.username'),
            Column('answer', String(250), nullable=False),
            Column('date', DateTime, nullable=False)
        )
