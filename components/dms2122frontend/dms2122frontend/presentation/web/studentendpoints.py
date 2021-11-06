""" StudentEndpoints class module.
"""
import inspect
import json
import os
from dms2122frontend import g
from typing import Text, Union
from flask import redirect, url_for, session, render_template
from werkzeug.wrappers import Response

from dms2122frontend.data.questionMocks import getQuestionMocks
from dms2122common.data import Role
from dms2122frontend.data.rest.authservice import AuthService
import dms2122frontend
from .Question import Question
from .webauth import WebAuth


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
            name=name,
            roles=session["roles"],
            questions=db.getUnasweredQuestions(name),
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
        return render_template(
            "student/answered/answered.html",
            name=name,
            roles=session["roles"],
            questions=db.getAnsweredQuestions(name),
        )
