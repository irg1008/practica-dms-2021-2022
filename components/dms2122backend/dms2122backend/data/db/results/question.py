""" Question class module.
"""

from typing import Dict, List
from sqlalchemy import Table, MetaData, Column, String, Integer, Float, Boolean  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from dms2122backend.data.db.results.resultbase import ResultBase
from dms2122backend.data.db.results.userrole import UserRole
from answeredQuestion import AnsweredQuestion


class Question(ResultBase):
    """ Definition and storage of user ORM records.
    """

    def __init__(
        self,
        title: str,
        statement: str,
        correctOption: str,
        incorrectOptions: List[str],
        imageUrl: str = "",
        score: float = 0,
        penalty: float = 0,
        public: bool = True,
    ):
        """ Constructor method.

        Initializes a user record.

        Args:
            - username (str): A string with the user name.
            - password (str): A string with the password hash.
        """
        self.title: str = title
        self.statement: str = statement
        self.correctOption: str = correctOption
        self.incorrectOptions: List[str] = incorrectOptions
        self.imageUrl: str = imageUrl
        self.score: float = score
        self.penalty: float = penalty
        self.public: bool = public
        self.ncorrect: int = 0
        self.nanswered: int = 0

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
            "questions",
            metadata,
            Column("title", String(250), primary_key=True),
            Column("statement", String(250), nullable=False),
            Column("imageUrl", String(250), nullable=True),
            Column("correctOption", String(250), nullable=False),
            Column("incorrectOptions", String(), nullable=False),
            Column("score", Float, default=0),
            Column("penalty", Float, default=0),
            Column("public", Boolean, default=True),
            Column("ncorrect", Integer, default=0),
            Column("nanswered", Integer, default=0),
        )

    @staticmethod
    def _mapping_properties() -> Dict:
        """ Gets the mapping properties dictionary.

        Returns:
            - Dict: A dictionary with the mapping properties.
        """
        return {
            "answereds": relationship(AnsweredQuestion, backref="answeredQuestions")
        }
