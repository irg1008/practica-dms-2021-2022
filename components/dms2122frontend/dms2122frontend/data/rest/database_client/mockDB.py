import random
from typing import Dict, List, Union

from dms2122frontend.data.rest.database_client.database_client import DatabaseClient
from dms2122frontend.presentation.web.Question import AnsweredQuestion, Question
from dms2122frontend.data.questionMocks import getQuestionMocks


class mockDB(DatabaseClient):
    """
        Mock Database for the mock frontend
    """

    def __init__(self):
        questions = getQuestionMocks()
        slice_point = len(questions) // 2
        self.answered = self._mock_answer_questions(
            list(questions.values())[:slice_point]
        )
        self.not_answered = dict(list(questions.items())[slice_point:])
        self.questions = questions

    def getAnsweredQuestions(self, username: str) -> List[AnsweredQuestion]:
        return list(self.answered.values())

    def _mock_answer_questions(self, questions: List[Question]):
        ans: Dict[int, AnsweredQuestion] = {}
        for q in questions:
            if random.random() > 0.5:
                ans[q.id] = AnsweredQuestion(q, q.correct_answer)
            else:
                ans[q.id] = AnsweredQuestion(q, random.choice(q.incorrect_answers))

        return ans

    def getUnasweredQuestions(self, username: str) -> List[Question]:
        return list(self.not_answered.values())

    def answerQuestion(self, username: str, question_id: int, answer: str) -> bool:
        try:
            del self.not_answered[question_id]
            self.answered[question_id] = AnsweredQuestion(
                self.questions[question_id], answer
            )
            return True
        except:
            return False

    def getQuestion(self, question_id: int) -> Union[Question, None]:
        return self.questions.get(question_id)

    def getAnsweredQuestion(
        self, username: str, question_id: int
    ) -> Union[AnsweredQuestion, None]:
        return self.answered.get(question_id)

    def getAllQuestions(self) -> List[Question]:
        questions = list(self.questions.values())
        questions.sort(key=lambda q: q.number_of_questions_answered)

        return questions
