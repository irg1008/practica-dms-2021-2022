from typing import List, Tuple
from sqlalchemy.orm.session import Session  # type: ignore
from dms2122backend.data.db.results.question import Question  # type: ignore
from dms2122backend.data.db.results.answeredQuestion import AnsweredQuestion  # type: ignore
from dms2122backend.data.db.results.userStats import UserStats  # type: ignore
from dms2122backend.data.db.resultsets.dbmanager import DBManager
import json


class Questions:
    @staticmethod
    def editQuestion(session: Session, id: int, edited: Question) -> bool:
        session.begin()
        try:
            res = session.query(Question).filter_by(id=id)

            res.update(
                {
                    "title": edited.title,
                    "statement": edited.statement,
                    "correctOption": edited.correctOption,
                    "incorrectOptions": edited.incorrectOptions,
                    "imageUrl": edited.imageUrl,
                    "score": edited.score,
                    "penalty": edited.penalty,
                    "public": edited.public,
                }
            )
        except:
            session.rollback()
            return False
        else:
            session.commit()
            return True

    @staticmethod
    def _get_answered_questions(session: Session, iduser: str) -> Tuple[List[Question], List[AnsweredQuestion]]:
        a_q: List[AnsweredQuestion] = DBManager.select_by(
            AnsweredQuestion, session, iduser=iduser)

        a_q_ids = [a.idquestion for a in a_q]

        questions: List[Question] = []

        for id in a_q_ids:
            q = DBManager.first(Question, session, id=id)
            questions.append(q)

        return questions, a_q

    @staticmethod
    def get_answered(session: Session, iduser: str) -> Tuple[List[Question], List[AnsweredQuestion]]:
        """Retrieves the user answered questions

        Args:
            session (Session): Current Working Session
            userniduserame (str): User ID

        Raises:

        Returns:
            List[Question]: User's Answered Questions
        """
        session.begin()
        try:
            answered_questions = Questions._get_answered_questions(
                session, iduser)
        except:
            session.rollback()
            return ([], [])
        else:
            session.commit()
            return answered_questions

    @staticmethod
    def get_unanswered(session: Session, iduser: str) -> List[Question]:
        """Retrieves the user unanswered questions

        Args:
            session (Session): Current Working Session
            iduser (str): User ID

        Raises:

        Returns:
            List[Question]: User's Unanswered Questions
        """
        session.begin()
        try:
            all_questions: List[Question] = DBManager.list_all(
                session, Question)

            questions, _ = Questions._get_answered_questions(
                session, iduser)

            unanswered_questions: List[Question] = [
                q for q in all_questions if q not in questions]
        except:
            session.rollback()
            return []
        else:
            session.commit()
            return unanswered_questions

    @staticmethod
    def get_user_question_answer(session: Session, iduser: str, idquestion: int):
        """Retrieves the user answer to a certain question

        Args:
            session (Session): Current Working Session
            iduser (str): User ID
            idquestion (str): Question ID

        Raises:

        Returns:
            AnsweredQuestion: User's answer to a certain question
        """
        session.begin()
        try:
            a_q: AnsweredQuestion = DBManager.first(
                AnsweredQuestion, session, iduser=iduser, idquestion=idquestion)
        except:
            session.rollback()
            return None
        else:
            session.commit()
            return a_q

    @staticmethod
    def set_user_question_answer(session: Session, idquestion: int, iduser: str, answer: str):
        session.begin()
        try:
            # Aumentamos las veces que ha sido usada esa respuesta
            question = DBManager.first(Question, session, id=idquestion)

            if not question:
                session.rollback()
                return False

            aux = question.get_answer_stats()
            aux[answer] += 1
            question.answerStats = json.dumps(aux)
            session.flush()

            # Modificamos los stats del usuario que responde
            # Aumentamos el numero de respuestas

            userStat: UserStats = DBManager.first(
                UserStats, session, iduser=iduser)

            if userStat is None:
                session.rollback()
                return False

            userStat.nanswered = userStat.nanswered + 1
            session.flush()

            # Añadimos la puntuación obtenida
            if answer == question.correctOption:
                userStat.score = userStat.score + question.score
                session.flush()
                userStat.ncorrect = userStat.ncorrect + 1
                session.flush()
            else:
                userStat.score = userStat.score + question.penalty
                session.flush()
        except:
            session.rollback()
            return False
        else:
            session.commit()
            return True
