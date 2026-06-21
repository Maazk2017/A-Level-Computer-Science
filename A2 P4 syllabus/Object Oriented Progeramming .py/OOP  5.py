#Q3
#PART a
class Lesson():
    #PRIVATE LessonType :STRING
    #PRIVATE Instructor :STRING
    def __innit__(self,LessonType,Instructor):
        self.__LessonType=LessonType
        self.__Instructor=Instructor
#PART b
    def GetLessonType(self):
        return self.__LessonType
#PART c
    def GetFee(self,level):
        if level=="B":
            return 45
        elif level=="I":
            return 50
        elif level=="A":
            return 55
        else:
            return -1
#PART d
#*IMPORTANT
#DECLARE LessonArray : ARRAY[0:9] OF Lesson
LessonArray=[""]*9
#PART e
LessonArray[2]=Lesson("Improve your serve","David")


