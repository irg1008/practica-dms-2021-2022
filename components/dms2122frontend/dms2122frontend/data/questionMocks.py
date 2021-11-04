import json
from typing import List
import os
from dms2122frontend.presentation.web.Question import Question


def getQuestionMocks():

    path = os.path.dirname(__file__)

    questions: List[Question] = []
    file = open("")
    q_json = json.load()

    for q in q_json:
        questions.append(
            Question(
                q["id"],
                q["title"],
                q["statment"],
                q["correct_answer"],
                q["incorrect_answers"],
                q["imageUrl"],
                float(q["score"]),
                float(q["penalty"]),
                bool(q["isPublic"]),
            )
        )

    return questions
