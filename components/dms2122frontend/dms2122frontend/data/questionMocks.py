import inspect
import json
from typing import Dict, List
import os
import dms2122frontend
from dms2122frontend.presentation.web.Question import Question


def getQuestionMocks() -> Dict[int, Question]:

    questions = {}
    file = open(
        os.path.dirname(inspect.getfile(dms2122frontend)) + "/static/questions.json"
    )
    q_json = json.load(file)

    for q in q_json:
        questions[int(q["id"])] = Question(
            int(q["id"]),
            q["title"],
            q["statment"],
            q["correct_answer"],
            q["incorrect_answers"],
            q["user_answers"],
            q["imageUrl"],
            float(q["score"]),
            float(q["penalty"]),
            bool(q["is_public"]),
        )

    return questions
