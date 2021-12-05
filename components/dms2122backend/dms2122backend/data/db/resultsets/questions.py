from sqlalchemy.orm.session import Session  # type: ignore
from dms2122backend.data.db.results.question import Question
from dms2122backend.data.db.results.userStats import UserStats
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
    def updateUserAnswer(session: Session, idquestion: int, iduser: str, answer: str):
        session.begin()
        try:
            # Aumentamos las veces que ha sido usada esa respuesta
            question = session.query(Question).filter_by(id=idquestion).first()

            if not question:
                session.rollback()
                return False

            aux = question.get_answer_stats()
            aux[answer] += 1
            question.answerStats = json.dumps(aux)
            session.flush()

            # Modificamos los stats del usuario que responde
            ## Aumentamos el numero de respuestas

            userStat = session.query(UserStats).filter_by(id=iduser).first()

            if not userStat:
                session.rollback()
                return False

            userStat.nanswered = userStat.nanswered + 1
            session.flush()

            ## Añadimos la puntuación obtenida
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
