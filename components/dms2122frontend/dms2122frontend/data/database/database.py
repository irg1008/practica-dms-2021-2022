from typing import List, Union

from dms2122frontend.presentation.web.Question import Question, AnsweredQuestion


class Database:
    """
    Databse Adapter Interface
    """

    def getAnsweredQuestions(self, username: str) -> List[AnsweredQuestion]:
        raise Exception("Not Implemented")
        return []

    def getUnasweredQuestions(self, username: str) -> List[Question]:
        raise Exception("Not Implemented")
        return []

    def answerQuestion(self, username: str, question_id: int, answer: str) -> bool:
        raise Exception("Not Implemented")
        return False

    def getQuestion(self, question_id: int) -> Union[Question, None]:
        raise Exception("Not Implemented")
        pass

    def getAnsweredQuestion(
        self, username: str, question_id: int
    ) -> Union[AnsweredQuestion, None]:
        raise Exception("Not Implemented")
        pass
