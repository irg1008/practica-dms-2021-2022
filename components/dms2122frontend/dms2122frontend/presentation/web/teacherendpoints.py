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

def create_question_from_form():
    # Create quesiton.
    id = get_db().getCurrentQuestionId()
    title = request.form.get("title") or ""
    statment = request.form.get("statment") or ""
    score = request.form.get("score") or ""
    penalty = request.form.get("penalty") or ""
    image_url = request.form.get("image_url") or ""
    correct_answer = ""
    incorrect_answers = []

    q = Question(id, title, statment, correct_answer,
                    incorrect_answers, score, penalty, image_url)
    
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

        return render_template("teacher/new/newQuestion.html", question=q)

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

        # Get quesiton.
            # question = get_db().createQuestion(title, statment, correct_answer, incorrect_answers, image_url, score, penalty)

        n_answers = request.form.get("numberOfAnswers") or 0

        return render_template("teacher/new/confirmQuestion.html", n_answers=int(n_answers))
    
    # Add confirm qustion after input answers
