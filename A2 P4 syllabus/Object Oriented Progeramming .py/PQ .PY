class Picture():
    def __init__(self,Des,Wid,Hei,FC):
        self.__Description=Des
        self.__Height=Hei
        self.__Width=Wid
        self.__FrameColour=FC
    def GetDescription(self):
        self.__Description
    def GetHeight(self):
        return self.__Height
    def GetWidth(self):
        return self.__Width
    def SetColour(self):
        return self.__FrameColour
    def SetDescription(self,newdes):
         self.__Description=newdes


class TreasureChest():
    def __init__(self,Que,Ans,Poi):
        self.__Question=Que
        self.__Answer=Ans
        self.__Points=Poi
    def getQuestion(self):
        return self.__Question
    def checkAnswer(self,userans):
        userans=input("Enter Correct Answer:")
        if userans==userans.Answer():
            return True
        else:
            return False
    def getPoints(self,attempts):
        if attempts==1:
            return self.__Points
        elif attempts==2:
            temp=int(self.Points/2)
            return temp
        elif attempts==3 or attempts==4:
            temp_1=int(self.__Points/4)
            return temp_1
        else:
            return 0

class Balloon():
    def __init__(self,DefItem,Col):
        self.__DefenceItem=DefItem
        self.__Colour=Col
        self.__Health=100
    def GetDefenceItem(self):
        return self.__DefenceItem
    def ChangeHealth(self,newhp):
        self.__Health=self.__Health+newhp
    def CheckHealth(self):
        if self.__Health<=0:
            return True
        else:
            return False
    def GetHealth(self):
        return self.__Health
userdef=input("Enter a DefenceItem:")
usercol=input("Enter a Colour:")
Balloon1=Balloon(userdef,usercol)
def Defend(BalloonObject):
    inpstr=int(input("Enter The Strenght:"))
    BalloonObject.ChangeHealth(-inpstr)
    print("The Defence Item is :",BalloonObject.GetDefenceItem())
    checker=BalloonObject.CheckHealth()
    if checker==True:
        print("No Health Remaining:")
    else:
        print("Health Reamining:")
    return BalloonObject
Balloon1=Defend(Balloon1)
print("Health Left:",Balloon1.GetHealth())

class Lesson():
    def __init__(self,LessonTypeP,InstructorP):
        self.__LessonType=LessonTypeP
        self.__Instructor=InstructorP
    def GetLessonType(self):
        return self.__LessonType
    def GetFee(self,char):
        if char=="B":
            return 45
        elif char=="I":
            return 50
        elif char=="A":
            return 55
        else:
            return -1
    def SetLessonType(self,NewLesson):
        self.__LessonType=NewLesson
    #DECLARE LessonArray:[0:8] OF Lesson
    LessonArray=[""]*9
    LessonArray[2]=Lesson("Improve Your Serve","David")
    LessonArray[2].SetLessonType("Object OOP Class","Taha")
    print(LessonArray[2].GetLessonType())



          
        
    
