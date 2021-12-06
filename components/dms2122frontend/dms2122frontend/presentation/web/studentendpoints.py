""" StudentEndpoints class module.
"""
import inspect
import json
import os
from dms2122frontend import g
from typing import Dict, List, Text, Union
from flask import redirect, request, url_for, session, render_template
from werkzeug.wrappers import Response

from dms2122frontend.data.questionMocks import getQuestionMocks
from dms2122common.data import Role
from dms2122frontend.data.rest.authservice import AuthService
import dms2122frontend
from .webauth import WebAuth
from dms2122frontend.g import get_db


class StudentEndpoints:
    """ Monostate class responsible of handling the student web endpoint requests.
    """

    @staticmethod
    def get_student(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the student root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for("get_login"))
        if Role.Student.name not in session["roles"]:
            return redirect(url_for("get_home"))
        name = session["user"]

        questions = getQuestionMocks()
        db = g.get_db()
        return render_template(
            "student/student.html",
            questions=db.getUnasweredQuestions(name, token=session.get("token")),
        )

    @staticmethod
    def get_student_answered(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to /student/answered

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for("get_login"))
        if Role.Student.name not in session["roles"]:
            return redirect(url_for("get_home"))
        name = session["user"]

        db = g.get_db()
        stats = db.getUserStats(session["user"], session["token"])
        ans = db.getAnsweredQuestions(name, token=session.get("token"))
        ans.sort(key=lambda x: x.date, reverse=True)

        total_questions = len(ans)
        total_correct = len(list(filter(lambda a: a.is_correct_answer(), ans)))
        total_score = sum([a.score for a in ans])

        return render_template(
            "student/answered/answered.html",
            roles=session["roles"],
            questions=ans,
            total_score=stats.get("score") or 0,
            total_correct=stats.get("ncorrect") or 0,
            total_questions=stats.get("nanswered") or 0,
        )

    @staticmethod
    def post_student_answers(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the POST requests to /student/answered

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for("get_login"))
        if Role.Student.name not in session["roles"]:
            return redirect(url_for("get_home"))

        username = session["user"]
        db = g.get_db()

        for q_id, ans in request.form.items():
            res = db.answerQuestion(
                username, int(q_id), ans, token=session.get("token")
            )

        return redirect(url_for("get_student_answered"))

    @staticmethod
    def get_student_iterator(
        auth_service: AuthService, q_pos: int
    ) -> Union[Response, Text]:
        """ Handles the POST requests to /student/iterator/<int>

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for("get_login"))
        if Role.Student.name not in session["roles"]:
            return redirect(url_for("get_home"))

        ans: Dict[str, str] = session["answered"]
        questions: List[str] = session["toanswer"]

        # Get and update the posted questions:
        items = list(request.form.items())

        # To review:
        if len(items) == 2:
            q_id, user_ans = items[0]
            ans[q_id] = user_ans
        elif len(items) == 1:
            _, q_id = items[0]
            if q_id in ans:
                del ans[q_id]

        if q_pos < 0 or q_pos >= len(questions):
            return "Bad Position"
        db = get_db()
        question = db.getQuestion(int(questions[q_pos]), token=session.get("token"))

        if not question:
            return "No question"

        selected_ans = ans.get(str(question.id))

        return render_template(
            "student/iterator/iterator.html",
            questionId=question.id,
            quest=question,
            prev=(None if q_pos - 1 < 0 else str(q_pos - 1)),
            next=None if q_pos + 1 >= len(questions) else str(q_pos + 1),
            isLast=q_pos == len(questions) - 1,
            answer=selected_ans,
        )

    @staticmethod
    def post_student_iterator(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the POST requests to /student/iterator

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for("get_login"))
        if Role.Student.name not in session["roles"]:
            return redirect(url_for("get_home"))
        username = session["user"]
        session["answered"] = request.form.to_dict()
        session["toanswer"] = [
            q.id
            for q in get_db().getUnasweredQuestions(
                username, token=session.get("token")
            )
        ]
        return redirect(url_for("post_student_iterator_value", it=0))

    @staticmethod
    def post_student_iterator_submit(
        auth_service: AuthService,
    ) -> Union[Response, Text]:
        """ Handles the POST requests to /student/iterator

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for("get_login"))
        if Role.Student.name not in session["roles"]:
            return redirect(url_for("get_home"))

        ans: Dict[str, str] = session["answered"]

        db = g.get_db()

        username = session["user"]

        q_id, user_ans = list(request.form.items())[0]

        ans[q_id] = user_ans

        for q_id, user_ans in ans.items():

            try:
                db.answerQuestion(
                    username, int(q_id), user_ans, token=session.get("token")
                )
            except:
                print(f"Error while casting to int {q_id}", flush=True)

        session["answered"] = None
        session["toanswer"] = None

        return redirect(url_for("get_student_answered"))
