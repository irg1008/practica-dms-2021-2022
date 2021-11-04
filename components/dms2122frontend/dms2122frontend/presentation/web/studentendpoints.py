""" StudentEndpoints class module.
"""
import inspect
import json
import os
from typing import Text, Union
from flask import redirect, url_for, session, render_template
from werkzeug.wrappers import Response
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

        questions = []
        file = open(os.path.dirname(inspect.getfile(dms2122frontend)) + "/static/questions.json")
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

        return render_template(
            "student.html",
            name=name,
            roles=session["roles"],
            questions=questions,
        )
