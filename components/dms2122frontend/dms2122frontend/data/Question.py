# Import the datetime
import datetime

# A class named Question with the next variables:
# - id
# - title
# - statment
# - correct answer
# - incorrect answers
# - score
# - penalty
# - isPublic
# - number of correct answers
# - number of questions answered
# All variables should be typed using typing library
# This class has the next functions:
# - A function that gets the total score.
# - A function that receives an answer and returns score or penalty. This function also increments number of correct answers and number of questions answered.


class Question:
    def __init__(self, id, title, statement, correctAnswer, incorrectAnswers, score, penalty, isPublic):
        self.id = id
        self.title = title
        self.statement = statement
        self.correctAnswer = correctAnswer
        self.incorrectAnswers = incorrectAnswers
        self.score = score
        self.penalty = penalty
        self.isPublic = isPublic
        self.numberOfCorrectAnswers = 0
        self.numberOfQuestionsAnswered = 0

    def getTotalScore(self):
        return self.score * self.numberOfCorrectAnswers - self.penalty * self.numberOfQuestionsAnswered

    def receiveAnswer(self, answer):
        self.numberOfQuestionsAnswered += 1

        if answer == self.correctAnswer:
            self.numberOfCorrectAnswers += 1
            return self.score
        else:
            return -self.penalty


# A class named AnsweredQuestion that contains the next variables:
# - A question. This is a Question object.
# - An answer. We will later check is correct with the question function.
# - An score
# - A date. This should be added automatically when an answer is provided.
# This class has the next functions:
# - Answer. This function recieves an answer and check if is correct with the question variable and recieveAnswer method.
class AnsweredQuestion:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.score = self.question.recieveAnswer(answer)
        self.date = datetime.datetime.now()

        # A function that check answer is correct with the question variable and recieveAnswer method.
        def isCorrectAnswer(self):
            return self.answer == self.question.correctAnswer
