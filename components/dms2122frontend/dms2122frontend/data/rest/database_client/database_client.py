from typing import List, Tuple, Union

from dms2122frontend.data.Question import Question, AnsweredQuestion
from abc import ABC, abstractmethod


class DatabaseClient(ABC):
    """
    Databse Adapter Interface
    """

    @abstractmethod
    def getAnsweredQuestions(self, username: str, token="") -> List[AnsweredQuestion]:
        raise Exception("Not Implemented")

    @abstractmethod
    def getUnasweredQuestions(self, username: str, token="") -> List[Question]:
        raise Exception("Not Implemented")

    @abstractmethod
    def answerQuestion(
        self, username: str, question_id: int, answer: str, token=""
    ) -> bool:
        raise Exception("Not Implemented")

    @abstractmethod
    def getQuestion(self, question_id: int, token="") -> Union[Question, None]:
        raise Exception("Not Implemented")

    @abstractmethod
    def createQuestion(self, question: Question, token="") -> Tuple[Question, int]:
        raise Exception("Not Implemented")

    @abstractmethod
    def updateQuestion(self, Question: Question, token="") -> None:
        raise Exception("Not Implemented")

    @abstractmethod
    def getAnsweredQuestion(
        self, username: str, question_id: int, token=""
    ) -> Union[AnsweredQuestion, None]:
        raise Exception("Not Implemented")

    @abstractmethod
    def getAllQuestions(self, token="") -> List[Question]:
        raise Exception("Not Implemented")
