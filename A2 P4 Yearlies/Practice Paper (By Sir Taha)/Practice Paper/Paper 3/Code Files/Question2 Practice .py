#Part a
class QuestionClass():
    #PRIVATE Question:STRING
    #PRIVATE Answer:STRING
    #PRIVATE Difficulty:INTEGER
    def __init__(self,Question,Answer,Difficulty):
        self.__Question=Question 
        self.__Answer=Answer
        self.__Difficulty=Difficulty
#Part b
class Quiz():
    #PRIVATE Questions:QuestionClass
    #PRIVATE NumberOfQuestions:INTEGER
    def __init__(self):
        self.__Questions=[""]*20
        self.__NumberOfQuestions=0
#Part c
    def AddQuestion(self,question):
        if self.__NumberOfQuestions<20:
            self.__Questions[self.__NumberOfQuestions]=question
            self.__NumberOfQuestions=self.__NumberOfQuestions+1
            return True
        else:
            return False       
#Part d
Question1=QuestionClass("What is 100/5 ? :","20",1)
FirstQuiz=Quiz()
Temp=FirstQuiz.AddQuestion(Question1)
#Not in question just did it for testing
if Temp==False:
    print("Not Added")
else:
    print("Added")
