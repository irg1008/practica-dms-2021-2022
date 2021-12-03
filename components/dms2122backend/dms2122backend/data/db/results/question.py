""" Question class module.
"""

from typing import Dict, List
from sqlalchemy import Table, MetaData, Column, String, Integer, Float, Boolean  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from dms2122backend.data.db.results.resultbase import ResultBase
from dms2122backend.data.db.results.answeredQuestion import AnsweredQuestion
import json


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
        self.id: int
        self.title: str = title
        self.statement: str = statement
        self.correctOption: str = correctOption
        self.incorrectOptions: str = json.dumps(incorrectOptions)
        self.imageUrl: str = imageUrl
        self.score: float = score
        self.penalty: float = penalty
        self.public: bool = public

        # Create dictionary for answer stats.
        statsKeys = incorrectOptions + [correctOption]
        ansStats = dict.fromkeys(statsKeys, 0)

        # Transform dictionary to JSON string.
        ansStatsJson = json.dumps(ansStats)
        self.answerStats: str = ansStatsJson

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
            Column("id", Integer, primary_key=True, autoincrement="auto"),
            Column("title", String(250), nullable=False),
            Column("statement", String(250), nullable=False),
            Column("imageUrl", String(250), nullable=True),
            Column("correctOption", String(250), nullable=False),
            Column("incorrectOptions", String(), nullable=False),
            Column("score", Float, default=0),
            Column("penalty", Float, default=0),
            Column("public", Boolean, default=True),
            Column("answerStats", String(), nullable=False),
        )

    @staticmethod
    def _mapping_properties() -> Dict:
        """ Gets the mapping properties dictionary.

        Returns:
            - Dict: A dictionary with the mapping properties.
        """
        return {"answers": relationship(AnsweredQuestion, backref="answeredQuestions")}

    def __str__(self):
        return f"{self.id}, {self.statement}, {self.answerStats}"

    def __repr__(self) -> str:
        return self.__str__()
