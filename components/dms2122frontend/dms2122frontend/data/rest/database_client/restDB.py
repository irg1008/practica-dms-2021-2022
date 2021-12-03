from typing import Dict, List, Tuple, Union

import requests
from dms2122frontend.data.Question import Question
from dms2122frontend.data.Question import AnsweredQuestion
from dms2122frontend.data.rest.database_client.database_client import DatabaseClient
from dms2122frontend.data.rest.database_client.mockDB import mockDB


class RestDB(mockDB):
    def __init__(
        self, base_url: str, api_back_secret: str, api_back_header: str
    ) -> None:
        self.__base_url: str = base_url
        self.__api_back_secret: str = api_back_secret
        self.__api_back_header: str = api_back_header
        mockDB.__init__(self)

    def __check_token(self, token: str):
        if len(token) == 0 or len(token.split(".")) != 3:
            raise Exception("Invalid Token Format")

    def __get_headers(self, token: str) -> Dict:
        self.__check_token(token)
        return {
            "Authorization": f"Bearer {token}",
            self.__api_back_header: self.__api_back_secret,
        }

    # def getAnsweredQuestions(
    #     self, username: str, token: str = ""
    # ) -> List[AnsweredQuestion]:
    #     raise Exception("Not Implemented")
    #
    # def getUnasweredQuestions(self, username: str, token: str = "") -> List[Question]:
    #     raise Exception("Not Implemented")
    #     return []
    #
    # def answerQuestion(
    #     self, username: str, question_id: int, answer: str, token: str = ""
    # ) -> bool:
    #     raise Exception("Not Implemented")
    #
    def getQuestion(self, question_id: int, token: str = "") -> Union[Question, None]:
        res = requests.get(
            f"{self.__base_url}/question/{question_id}",
            headers=self.__get_headers(token),
        )

        if not res.ok:
            return None
        return Question.From_Json(res.json())

    #
    # def getCurrentQuestionId(self, token="") -> int:
    #     raise Exception("Not Implemented")
    #
    # def createQuestion(
    #     self, question: Question, token: str = ""
    # ) -> Tuple[Question, int]:
    #     raise Exception("Not Implemented")
    #
    # def updateQuestion(self, Question: Question, token: str = "") -> None:
    #     raise Exception("Not Implemented")
    #
    # def getAnsweredQuestion(
    #     self, username: str, question_id: int, token: str = ""
    # ) -> Union[AnsweredQuestion, None]:
    #     raise Exception("Not Implemented")

    def getAllQuestions(self, token: str = "") -> List[Question]:
        res = requests.get(
            f"{self.__base_url}/question/all", headers=self.__get_headers(token)
        )

        if not res.ok:
            return []

        return [Question.From_Json(q) for q in res.json()]

