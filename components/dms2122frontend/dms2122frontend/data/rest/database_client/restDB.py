
from typing import Dict, List, Tuple, Union

import requests
from dms2122frontend.data.Question import Question
from dms2122frontend.data.Question import AnsweredQuestion
from dms2122frontend.data.rest.database_client.database_client import DatabaseClient


class RestDB(DatabaseClient):

    def __init__(self, base_url: str, api_back_secret: str,api_back_header: str) -> None:
        self.__base_url:str = base_url
        self.__auth_secret:str = api_back_secret
        self.__api_back_header: str = api_back_header

    def __check_token(self, token: str):
        if len(token) == 0 or len(token.split(".")) != 3:
            raise Exception("Invalid Token Format")

    def __get_header(self, token: str) -> Dict:
        return  {"Authorization": f"Bearer {token}",
                self.__api_back_header: self.__api_back_header}

    def getAnsweredQuestions(self, username: str, token="") -> List[AnsweredQuestion]:
        raise Exception("Not Implemented")

    
    def getUnasweredQuestions(self, username: str, token="") -> List[Question]:
        raise Exception("Not Implemented")
        return []

    def answerQuestion(self, username: str, question_id: int, answer: str, token="") -> bool:
        raise Exception("Not Implemented")
    

    def getQuestion(self, question_id: int, token="") -> Union[Question, None]:
        raise Exception("Not Implemented")
        

    def getCurrentQuestionId(self, token="") -> int:
        raise Exception("Not Implemented")


    def createQuestion(self, question: Question, token="") -> Tuple[Question, int]:
        raise Exception("Not Implemented")


    def updateQuestion(self, Question: Question, token="") -> None:
        raise Exception("Not Implemented")


    def getAnsweredQuestion(
        self, username: str, question_id: int, token=""
    ) -> Union[AnsweredQuestion, None]:
        raise Exception("Not Implemented")
        

    def getAllQuestions(self, token="") -> List[Question]:
        
        self.__check_token(token)

        res = requests.get(f"{self.__base_url}/question/all", self.__get_header(token))

        if not res.ok:
            return []


        return []