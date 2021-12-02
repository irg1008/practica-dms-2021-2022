""" Question class module.
"""

from typing import Dict, List
from sqlalchemy import Table, MetaData, Column, String, Integer, Float, Boolean  # type: ignore
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey  # type: ignore
from dms2122backend.data.db.results.resultbase import ResultBase
from dms2122backend.data.db.results.answeredQuestion import AnsweredQuestion


class UserStats(ResultBase):
    """ Definition and storage of user ORM records.
    """

    def __init__(
        self,
        iduser: str
    ):
        """ Constructor method.

        Initializes a user record.

        Args:
            - iduser (str): A string with the user name.
            - naswered (int): number of answered questions.
            - ncorrect (int): number of correct answered questions.
            - score (float): score of the user
        """
        self.iduser: str = iduser
        self.nanswered: int = 0
        self.ncorrect: int = 0
        self.score: float = 0

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
            "userStats",
            metadata,
            Column("iduser", String(32), ForeignKey('users.name'), primary_key=True),
            Column("naswered", Integer, default=0),
            Column("ncorrect", Integer, default=0),
            Column("score", Float, default=0)
        )
