""" TeacherEndpoints class module.
"""

from typing import List, Text, Union
from flask import redirect, url_for, session, render_template
from flask.globals import request
from werkzeug.wrappers import Response
from dms2122frontend.data.Question import Question
from dms2122common.data import Role
from dms2122frontend.data.rest.authservice import AuthService
from .webauth import WebAuth
from dms2122frontend.g import get_db
from dms2122common.data.rest import ResponseData


def get_id_from_params() -> int:
    str_id = request.args.get("q")
    return int(str(str_id)) if str_id is not None else -1


def create_question_from_form(id_from_param: bool = False) -> Question:
    # Create quesiton.
    id = get_id_from_params() if id_from_param else -1
    title = request.form.get("title") or ""
    statement = request.form.get("statement") or ""

    score = request.form.get("score")
    score = float(score) if score is not None else 1

    penalty = request.form.get("penalty")
    penalty = float(penalty) if penalty is not None else 0

    image_url = request.form.get("imageUrl") or ""
    correct_answer = ""
    incorrect_answers: List[str] = []

    q = Question(
        id,
        title,
        statement,
        correct_answer,
        incorrect_answers,
        image_url,
        score,
        penalty,
    )

    return q


def add_answers_to_question(q: Question) -> None:
    answers: List[str] = list(request.form.values())
    q.correct_answer = answers[0]
    q.incorrect_answers = answers[1:]


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

        questions = get_db().getAllQuestions(token=session.get("token"))

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
    def get_user_stats(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET a user list to show the stats

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for("get_login"))
        if Role.Teacher.name not in session["roles"]:
            return redirect(url_for("get_home"))

        

        return render_template("teacher/stats/stats.html")



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

        return render_template(
            "teacher/new/answersQuestion.html", n_answers=int(n_answers)
        )

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
        add_answers_to_question(q)
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
        get_db().createQuestion(q, token=session.get("token"))
        remove_session_question()

        ResponseData().add_message("Question created successfully")

        return redirect(url_for("get_teacher"))

    @staticmethod
    def get_edit_question(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the teacher root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """

        q_id: int = get_id_from_params()
        q = get_db().getQuestion(int(q_id), token=session.get("token"))

        # Make sure questions has no answers.
        if q is None or q.number_of_questions_answered > 0:
            return redirect(url_for("get_teacher"))

        return render_template("teacher/edit/editQuestion.html", q=q)

    @staticmethod
    def post_edit_question(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the teacher root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        q = create_question_from_form(id_from_param=True)
        ori_q = get_db().getQuestion(q.id, token=session.get("token"))

        if ori_q is None:
            return redirect(url_for("get_edit_question"))

        # TODO: Clean this up and delete duplicate code.
        # Adding answers.
        # +1 for correct answer.
        number_of_answers = len(ori_q.incorrect_answers) + 1
        answers: List[str] = list(request.form.values())[-number_of_answers:]
        q.correct_answer = answers[0]
        q.incorrect_answers = answers[1:]

        get_db().updateQuestion(q, token=session.get("token"))

        return redirect(url_for("get_teacher"))
