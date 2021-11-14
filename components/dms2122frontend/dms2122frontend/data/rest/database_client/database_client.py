from typing import List, Tuple, Union

from dms2122frontend.presentation.web.Question import Question, AnsweredQuestion


class DatabaseClient:
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
    
    def getCurrentQuestionId(self) -> int:
        raise Exception("Not Implemented")
        return 0

    def createQuestion(self, question: Question) -> Tuple[Question, int]:
        raise Exception("Not Implemented")
        return None

    def getAnsweredQuestion(
        self, username: str, question_id: int
    ) -> Union[AnsweredQuestion, None]:
        raise Exception("Not Implemented")
        pass

    def getAllQuestions(self) -> List[Question]:
        raise Exception("Not Implemented")
