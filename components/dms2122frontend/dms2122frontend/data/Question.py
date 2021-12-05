# Import the datetime
from abc import abstractclassmethod
from datetime import datetime
from typing import Any, Dict, List, Union
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


class SerializableQuestion:
    @staticmethod
    @abstractclassmethod
    def From_JSON(json_q: Union[str, Dict]) -> Any:
        raise NotImplemented

    @abstractclassmethod
    def to_JSON(self) -> str:
        raise NotImplemented

    @abstractclassmethod
    def to_JSON_dict(self) -> Dict[str, Any]:
        raise NotImplemented


class Question(SerializableQuestion):
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

        if not isinstance(incorrect_answers, list):
            raise Exception(
                f"Incorrect Answers is not a list, , is a {type(incorrect_answers)} - {incorrect_answers}"
            )

        if not isinstance(user_answers, dict):
            if isinstance(user_answers, str):
                user_answers = json.loads(user_answers)
            else:
                raise Exception(
                    f"User Answers is not a dict, is a {type(user_answers)} - {user_answers}"
                )

        self.id = id
        self.title = title
        self.statement = statement
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
        self.score = score
        self.penalty = penalty
        self.image_url = image_url
        self.number_of_correct_answers = int(
            user_answers.get(correct_answer) or 0)
        self.number_of_questions_answered = sum(
            [int(user_answers.get(ans) or 0) for ans in incorrect_answers]
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
        return json.dumps(self.to_JSON_dict())

    def to_JSON_dict(self) -> Dict[str, Any]:
        return {
            "id": str(self.id),
            "title": self.title,
            "statement": self.statement,
            "correct_answer": self.correct_answer,
            "incorrect_answers": self.incorrect_answers,
            "image_url": self.image_url,
            "score": self.score,
            "penalty": self.penalty,
            "user_answers": self.user_answers,
        }

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

    @staticmethod
    def From_error(error: str, status: int):
        return Question(
            id=-status,
            title="An error has ocurred",
            statement=error,
            correct_answer=error,
            penalty=0,
            image_url="",
            incorrect_answers=[],
            score=status,
        )


# A class named AnsweredQuestion that contains the next variables:
# - A question. This is a Question object.
# - An answer. We will later check is correct with the question function.
# - An score
# - A date. This should be added automatically when an answer is provided.
# This class has the next functions:
# - Answer. This function receives an answer and check if is correct with the question variable and recieveAnswer method.
class AnsweredQuestion(SerializableQuestion):
    def __init__(self, question: Question, answer: str, date: int = None):
        self.question = question
        self.answer = answer
        self.score = self.question.receive_answer(answer)
        self.date = datetime.fromtimestamp(date) if date else datetime.now()

        # A function that check answer is correct with the question variable and receive_answer method.

    def is_correct_answer(self):
        return self.answer == self.question.correct_answer

    @staticmethod
    def From_Json(json_q: Union[str, Dict]):
        if isinstance(json_q, str):
            d = json.loads(json_q)
        else:
            d = json_q

        return AnsweredQuestion(
            Question.From_Json(json_q), d["answer"], int(d["date"])
        )

    def to_JSON(self) -> str:
        return json.dumps(self.to_JSON_dict())

    def to_JSON_dict(self) -> Dict[str, Any]:
        return {
            "question": self.question.to_JSON_dict(),
            "answer": self.answer,
            "date": datetime.timestamp(self.date),
        }
