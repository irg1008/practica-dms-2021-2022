# Import the datetime
import datetime
from typing import Dict, List, Union
import random
import json

# A class named Question with the next variables:
# - id
# - title
# - statment
# - correct answer
# - incorrect answers
# - score
# - penalty
# - is_public
# - number of correct answers
# - number of questions answered
# All variables should be typed using typing library
# This class has the next functions:
# - A function that gets the total score.
# - A function that receives an answer and returns score or penalty. This function also increments number of correct answers and number of questions answered.


class Question:
    def __init__(
        self,
        id: int,
        title: str,
        statement: str,
        correct_answer: str,
        incorrect_answers: List[str],
        image_url: str,
        score: float,
        penalty: float,
        user_answers: Dict[str, int] = {},
    ):
        self.id = id
        self.title = title
        self.statement = statement
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
        self.score = score
        self.penalty = penalty
        self.image_url = image_url

        self.number_of_correct_answers = user_answers.get(correct_answer) or 0
        self.number_of_questions_answered = sum(
            [user_answers.get(ans) or 0 for ans in incorrect_answers]
        )
        self.is_public = True
        self.user_answers = user_answers

    def is_editable(self):
        return self.number_of_questions_answered == 0

    def get_answers(self, shuffle=False) -> List[str]:
        questions = list([self.correct_answer]) + self.incorrect_answers

        if shuffle:
            random.shuffle(questions)
        else:
            questions = sorted(questions)

        return questions

    def get_times_answered(self, answer: str) -> int:
        return self.user_answers.get(answer) or 0

    def get_total_score(self) -> float:
        return (
            self.score * self.number_of_correct_answers
            - self.penalty
            / 100
            * self.score
            * (self.number_of_questions_answered - self.number_of_correct_answers)
        )

    def receive_answer(self, answer: str):
        self.number_of_questions_answered += 1

        # Add user answer to question log.
        old = self.user_answers.get(answer) or 0
        self.user_answers[answer] = old + 1
        if answer == self.correct_answer:
            self.number_of_correct_answers += 1
            return self.score
        else:
            return -self.penalty / 100 * self.score

    def make_private(self):
        if len(self.user_answers) == 0:
            self.is_public = False

    def make_public(self):
        self.is_public = True

    def to_JSON(self) -> str:
        d = {
            "id": str(self.id),
            "title": self.title,
            "statement": self.statement,
            "correct_answer": self.correct_answer,
            "incorrect_answers": self.incorrect_answers,
            "image_url": self.image_url,
            "score": str(self.score),
            "penalty": str(self.penalty),
            "user_answer": json.dumps(self.user_answers),
        }
        return json.dumps(d)

    @staticmethod
    def From_Json(json_q: Union[str, Dict]) -> "Question":

        if isinstance(json_q, str):
            d = json.loads(json_q)
        else:
            d = json_q

        return Question(
            id=int(d["id"]),
            title=d["title"],
            statement=d["statement"],
            correct_answer=d["correct_answer"],
            incorrect_answers=d["incorrect_answers"],
            image_url=d["image_url"],
            score=float(d["score"]),
            penalty=float(d["penalty"]),
            user_answers=d["user_answers"],
        )


# A class named AnsweredQuestion that contains the next variables:
# - A question. This is a Question object.
# - An answer. We will later check is correct with the question function.
# - An score
# - A date. This should be added automatically when an answer is provided.
# This class has the next functions:
# - Answer. This function receives an answer and check if is correct with the question variable and recieveAnswer method.
class AnsweredQuestion:
    def __init__(self, question: Question, answer: str):
        self.question = question
        self.answer = answer
        self.score = self.question.receive_answer(answer)
        self.date = datetime.datetime.now()

        # A function that check answer is correct with the question variable and receive_answer method.

    def is_correct_answer(self):
        return self.answer == self.question.correct_answer

