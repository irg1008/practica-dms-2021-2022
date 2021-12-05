from sqlalchemy.orm.session import Session # type: ignore
from components.dms2122backend.dms2122backend.data.db.results.question import Question
from components.dms2122backend.dms2122backend.data.db.results.userStats import UserStats
from dbmanager import DBManager
import json

class Questions:
    @staticmethod
    def editQuestion(session: Session, id: int, edited: Question) -> bool:
        session.begin()
        try:
            a = session.query(Question).filter_by(id=id)
            a.update({column: getattr(edited, column) for column in Question.table.columns.keys()})
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
            question: Question = Question.query.filter_by(id=idquestion).first()
            aux = question.get_answer_stats()
            aux[answer] += 1
            question.answerStats = json.dumps(aux)
            session.flush()
            
            # Modificamos los stats del usuario que responde
            ## Aumentamos el numero de respuestas
            userStat: UserStats = Question.query.filter_by(id=iduser).first()
            userStat.nanswered = UserStats.nanswered + 1
            session.flush()
            
            ## Añadimos la puntuación obtenida
            if(answer == question.correctOption):
                userStat.score = UserStats.score + question.score
                session.flush()
                userStat.ncorrect = UserStats.ncorrect + 1
                session.flush()
            else:
                userStat.score = UserStats.score + question.penalty
                session.flush()
        except:
            session.rollback()
            return False
        else:
            session.commit()
            return True