import inspect
import json
from typing import List
import os
import dms2122frontend
from dms2122frontend.presentation.web.Question import Question


def getQuestionMocks() -> List[Question]:

    questions = []
    file = open(
        os.path.dirname(inspect.getfile(dms2122frontend)) + "/static/questions.json"
    )
    q_json = json.load(file)

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
