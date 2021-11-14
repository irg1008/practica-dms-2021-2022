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


def create_question_from_form() -> Question:
    # Create quesiton.
    id = get_db().getCurrentQuestionId()
    title = request.form.get("title") or ""
    statement = request.form.get("statement") or ""

    score = request.form.get("score")
    score = float(score) if score is not None else 1

    penalty = request.form.get("penalty")
    penalty = float(penalty) if penalty is not None else 0

    image_url = request.form.get("imageUrl") or ""
    correct_answer = ""
    incorrect_answers = []

    q = Question(id, title, statement, correct_answer,
                 incorrect_answers, image_url, score, penalty)

    return q


def update_session(q) -> None:
    session["question"] = q.to_JSON()


def check_session_question() -> bool:
    return "question" in session


def get_session_question() -> Question:
    question_str = session["question"]
    return Question.From_Json(question_str)


def remove_session_question() -> None:
    session["question"] = None


class TeacherEndpoints:
    """ Monostate class responsible of handing the teacher web endpoint requests.
    """

    @staticmethod
    def get_post_teacher(auth_service: AuthService) -> Union[Response, Text]:
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

        q = create_question_from_form()
        update_session(q)
        n_answers = request.form.get("numberOfAnswers") or 0

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

        q = get_session_question()
        answers = list(request.form.values())
        q.correct_answer = answers[0]
        q.incorrect_answers = answers[1:]
        update_session(q)

        return render_template("teacher/new/previewQuestion.html", q=q)

    @staticmethod
    def get_post_confirm_question(auth_service: AuthService) -> Union[Response, Text]:
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

        q = get_session_question()
        get_db().createQuestion(q)
        remove_session_question()

        return redirect(url_for("get_teacher"))

