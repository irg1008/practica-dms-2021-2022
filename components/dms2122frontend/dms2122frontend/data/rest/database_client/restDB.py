from http import HTTPStatus
import json
from typing import Dict, List, Tuple, Union

import requests
from requests import status_codes
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

    def getAnsweredQuestions(
        self, username: str, token: str = ""
    ) -> List[AnsweredQuestion]:
        res = requests.get(
            f"{self.__base_url}/user/{username}/questions/unanswered",
            headers=self.__get_headers(token),
        )
        if not res.ok:
            return [
                AnsweredQuestion(
                    Question.From_error(
                        f"An error has ocurred - {res.content}", res.status_code
                    ),
                    "",
                )
            ]

        return [AnsweredQuestion.From_Json(q) for q in res.json()]

    def getUnasweredQuestions(self, username: str, token: str = "") -> List[Question]:
        res = requests.get(
            f"{self.__base_url}/user/{username}/questions/unanswered",
            headers=self.__get_headers(token),
        )

        if not res.ok:
            return [
                Question.From_error(
                    f"An error has ocurred - {res.content}", res.status_code
                )
            ]

        return [Question.From_Json(q) for q in res.json()]

    def answerQuestion(
        self, username: str, question_id: int, answer: str, token: str = ""
    ) -> bool:
        res = requests.post(
            f"{self.__base_url}/user/{username}/questions/answer/{question_id}",
            headers=self.__get_headers(token),
            json={"answer": answer},
        )

        if not res.ok:
            return False

        return True

    def getQuestion(self, question_id: int, token: str = "") -> Question:
        res = requests.get(
            f"{self.__base_url}/question/{question_id}",
            headers=self.__get_headers(token),
        )

        if not res.ok:
            return Question.From_error("There was an error", res.status_code)

        return Question.From_Json(res.json())

    def createQuestion(
        self, question: Question, token: str = ""
    ) -> Tuple[Question, int]:

        res = requests.post(
            f"{self.__base_url}/question/new",
            headers=self.__get_headers(token),
            json=question.to_JSON_dict(),
        )

        if not res.ok:
            print(
                f"There was an error while creating the question - {res.content}",
                flush=True,
            )
            return (
                Question.From_error(
                    "There was an error while creating the question", res.status_code
                ),
                -res.status_code,
            )

        return question, int(res.content)

    def updateQuestion(self, question: Question, token: str = "") -> None:
        res = requests.patch(
            f"{self.__base_url}/question/{question.id}",
            headers=self.__get_headers(token),
            json=question.to_JSON_dict(),
        )

        if not res.ok:
            print(
                f"There was an error while creating the question - {res.content}",
                flush=True,
            )

    def getAllQuestions(self, token: str = "") -> List[Question]:
        res = requests.get(
            f"{self.__base_url}/question/all", headers=self.__get_headers(token)
        )

        if not res.ok:
            return []

        return [Question.From_Json(q) for q in res.json()]

