import random
from typing import List

from dms2122frontend.data.database.database import Database
from dms2122frontend.presentation.web.Question import AnsweredQuestion, Question
from dms2122frontend.data.questionMocks import getQuestionMocks


class mockDB(Database):
    """
        Mock Database for the mock frontend
    """

    def __init__(self):
        self.questions = getQuestionMocks()
        random.shuffle(self.questions)
        self.slice = random.randint(0, len(self.questions))

    def getAnsweredQuestions(self, username: str) -> List[AnsweredQuestion]:
        ans = []
        for q in self.questions[: self.slice]:
            if random.random() > 0.5:
                ans.append(AnsweredQuestion(q, q.correctAnswer))
            else:
                ans.append((AnsweredQuestion(q, random.choice(q.incorrectAnswers))))

        return ans

    def getUnasweredQuestions(self, username: str) -> List[Question]:
        return self.questions[self.slice :]
