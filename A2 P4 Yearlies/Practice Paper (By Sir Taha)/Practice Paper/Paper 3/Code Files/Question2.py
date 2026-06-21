class QuestionClass():
    #PRIVATE Question : STRING
    #PRIVATE Answer : STRING
    #PRIVATE Difficulty : INTEGER

    def __init__(self, QuestionP, AnswerP, DifficultyP):
        self.__Question = QuestionP
        self.__Answer = AnswerP
        self.__Difficulty = DifficultyP

    def GetQuestion(self):
        return self.__Question

    def GetDifficulty(self):
        return self.__Difficulty

    def GetAnswer(self):
        return self.__Answer


class QuizClass():
    #PRIVATE Questions : ARRAY [0:19] OF QuestionClass
    #PRIVATE NumberofQuestions : INTEGER
    def __init__(self):
        self.__Questions = [QuestionClass("","",0)] * 20
        self.__NumberofQuestions = 0

    def AddQuestion(self, QuestionObject):
        if self.__NumberofQuestions < 20:
            self.__Questions[self.__NumberofQuestions] = QuestionObject
            self.__NumberofQuestions = self.__NumberofQuestions + 1
            return True
        else:
            return False

Question1 = QuestionClass("What is 100/5 ?", "20", 1)

FirstQuiz = QuizClass()
FirstQuiz.AddQuestion(Question1)





