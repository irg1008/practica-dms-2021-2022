""" Question class module.
"""

from random import randint
from typing import Dict, List, Union
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
        mock_stats: bool = False,
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
        ansStats = dict.fromkeys(statsKeys, randint(0, 50) if mock_stats else 0)

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

    def to_JSON(self) -> str:
        d = {
            "id": str(self.id),
            "title": self.title,
            "statement": self.statement,
            "correct_answer": self.correctOption,
            "incorrect_answers": json.loads(self.incorrectOptions),
            "image_url": self.imageUrl,
            "score": str(self.score),
            "penalty": str(self.penalty),
            "user_answers": json.loads(self.answerStats),
        }
        return json.dumps(d)

    @staticmethod
    def From_Json(json_q: Union[str, Dict]) -> "Question":

        if isinstance(json_q, str):
            d = json.loads(json_q)
        else:
            d = json_q

        return Question(
            title=d["title"],
            statement=d["statement"],
            correctOption=d["correct_answer"],
            incorrectOptions=d["incorrect_answers"],
            imageUrl=d["image_url"],
            score=float(d["score"]),
            penalty=float(d["penalty"]),
        )

    def __str__(self):
        return f"{self.id}, {self.statement}, {self.answerStats}"

    def __repr__(self) -> str:
        return self.__str__()
