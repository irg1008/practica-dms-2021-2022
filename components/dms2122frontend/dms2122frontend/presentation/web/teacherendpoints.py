""" TeacherEndpoints class module.
"""

from typing import Text, Union
from flask import redirect, url_for, session, render_template
from flask.globals import request
from werkzeug.wrappers import Response
from dms2122frontend.presentation.web.Question import Question
from dms2122common.data import Role
from dms2122frontend.data.rest.authservice import AuthService
from .webauth import WebAuth
from dms2122frontend.g import get_db


# TODO: Use session question in all pages to not be forwarding to the same question.

def create_question_from_form():
    # Create quesiton.
    id = get_db().getCurrentQuestionId()
    title = request.form.get("title") or ""
    statement = request.form.get("statement") or ""

    score = request.form.get("score")
    score = int(score) if score is not None else 1

    penalty = request.form.get("penalty")
    penalty = int(penalty) if penalty is not None else 0

    image_url = request.form.get("image_url") or ""
    correct_answer = ""
    incorrect_answers = []

    q = Question(id, title, statement, correct_answer,
                 incorrect_answers, image_url, score, penalty)

    return q


class TeacherEndpoints:
    """ Monostate class responsible of handing the teacher web endpoint requests.
    """

    @staticmethod
    def get_teacher(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the teacher root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for("get_login"))
        if Role.Teacher.name not in session["roles"]:
            return redirect(url_for("get_home"))

        questions = get_db().getAllQuestions()

        return render_template("teacher/teacher.html", questions=questions)

    @staticmethod
    def get_post_new_question(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the teacher root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for("get_login"))
        if Role.Teacher.name not in session["roles"]:
            return redirect(url_for("get_home"))

        q = create_question_from_form()

        return render_template("teacher/new/newQuestion.html", q=q)

    @staticmethod
    def get_post_answers_question(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the teacher root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for("get_login"))
        if Role.Teacher.name not in session["roles"]:
            return redirect(url_for("get_home"))

        n_answers = request.form.get("numberOfAnswers") or 0

        # Save question to session on json format.
        q = create_question_from_form()
        session["question"] = q.to_JSON()

        return render_template("teacher/new/answersQuestion.html", n_answers=int(n_answers))

    @staticmethod
    def get_post_preview_question(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the teacher root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for("get_login"))
        if Role.Teacher.name not in session["roles"]:
            return redirect(url_for("get_home"))

        # Recover question from session.
        question_str = session["question"]
        q = Question.From_Json(question_str)

        answers = list(request.form.values())
        q.correct_answer = answers[0]
        q.incorrect_answers = answers[1:]

        # Update session with answers.
        session["question"] = q.to_JSON()

        return render_template("teacher/new/previewQuestion.html", q=q)
