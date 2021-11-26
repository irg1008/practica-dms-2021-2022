from typing import List
from dms2122frontend.data.questionMocks import getQuestionMocks
import random
from dms2122frontend.data.Question import Question, AnsweredQuestion

class User:
    def __init__(self, name: str, roles: List[str],) -> None:
        self.name = name
        self.roles = roles

        self.answeredQ, self.questions = self.__get_questions()

    def __get_questions(self):
        # Read the questions from the DB or something
        questions = getQuestionMocks()
        random.shuffle(questions)
        slice_point = random.randint(0, len(questions))

        answered = questions[:slice_point]
        unanswered = questions[slice_point:]

        return self.__aswerQuestions(answered), unanswered

    def __aswerQuestions(self, questions: List[Question]):
        ans = []
        for q in questions:
            if (random.random() > 0.5):
                ans.append(AnsweredQuestion(q, q.correct_answer))
            else:
                ans.append((AnsweredQuestion(q, random.choice(q.incorrect_answers))))

        return ans

