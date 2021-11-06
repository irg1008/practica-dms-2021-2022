from typing import List

from dms2122frontend.presentation.web.Question import Question, AnsweredQuestion


class Database:
    """
    Databse Adapter Interface
    """

    def getAnsweredQuestions(self, username: str) -> List[AnsweredQuestion]:
        pass

    def getUnasweredQuestions(self, username: str) -> List[Question]:
        pass
