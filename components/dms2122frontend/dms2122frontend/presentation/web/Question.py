# Import the datetime
import datetime
from typing import List
import random

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
        is_public: bool,
    ):
        self.id = id
        self.title = title
        self.statement = statement
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
        self.score = score
        self.penalty = penalty
        self.is_public = is_public
        self.image_url = image_url
        self.number_of_correct_answers = 0
        self.number_of_questions_answered = 0

    def get_answers(self, shuffle=False) -> List[str]:
        questions = list([self.correct_answer]) + self.incorrect_answers

        if shuffle:
            random.shuffle(questions)
        else:
            questions = sorted(questions)

        return questions

    def get_total_score(self):
        return (
            self.score * self.number_of_correct_answers
            - self.penalty * self.number_of_questions_answered
        )

    def receive_answer(self, answer: str):
        self.number_of_questions_answered += 1

        if answer == self.correct_answer:
            self.number_of_correct_answers += 1
            return self.score
        else:
            return -self.penalty


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
