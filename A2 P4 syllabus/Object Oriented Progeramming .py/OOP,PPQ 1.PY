#Q1 Part a
class Box():
    #PRIVATE size :STRING
    #DECLARE Contents:ARRAY[0:9] OF FieldObject
    #PRIVATE Lock:STRING
    #PRIVATE Stength:INTEGER
    def __init__(self,sze,item1,lok):
        self.__Size=sze
        self.__Contents=[]*9
        self.__Contents.append[item1]
        self.__Lock=lok
        self.__Strength=100
#Part b
    def GetStrength(self):
        return self.__Strength
    def Unlock(self,code):
        if code==self.__Lock:
            return True
        else:
            self.__Strength-1
            if self.__Strength<1:
              return True
            else:
              return False
#Part c














#Q3 Part a
class QuizClass():
    #DECLARE Question:ARRAY[0:19] OF QuestionClass
    #PRIVATE NumberofQuestions:INTEGER
    def __init__(self):
        self.__Questions=[]*19
        self.__NumberofQuestions=0
    def AddQuestion(self,QusetionObject):
        if self.__Questions<20:
            self.__Questions[self.__NumberofQuestions]=QusetionObject
            self.__NumberofQuestions=self.__NumberofQuestions+1
            return True
        else:
            return False
#Part b
#FirstQuiz=QuizClass()
#Question1=QuestionClass("What is 100/5","20",1)
#FirstQuiz.AddQuestion(Question1)


#Q4 Parta
class PuzzlePlayer():
    #PRIVATE PlayerID :STRING
    #PRIVATE Name:STRING
    #PRIVATE Score:INTEGER
    def __init__(self):
        self.__PlayerID="PL12a3"
        self.__Name=""
        self.__Score=0
#Part b
    def GetPlayerID(self):
        return self.__PlayerID
    def GetName(self):
        return self.__Name
    def GetScore(self):
        return self.__Score
#Part c
    def SetPlayerID(self,value):
        var=value
        if len(var)!=6 and var[0:2]!="PL":
            return False
        else:
            return True
        

#Q5 Parta
class FoodItem():
    #PRIVATE FoodID:STRING
    #PRIVATE Name:STRING
    #PRIVATE Calories:INTEGER
    def __init__(self,FoodID):
        self.__FoodID=FoodID
        self.__Name=""
        self.__Calories=0
#Par b
    def GetFoodID(self):
        return self.__FoodID
    def GetName(self):
        return self.__Name
    def GetCalories(self):
        return self.__Calories
#Part c
    def SetFoodID(self,newid):
        self.__FoodID=newid
    def SetName(self,newname):
        self.__Name=newname
    def SetCalories(self,newcal):
        if newcal>0 and newcal<2000:
            self.__Calories=newcal
            return True
        else:
            return False
        
#Q10 Part a
class Player():
    #PRIVATE Score:INTEGER
    #PRIVATE Category:STRING
    #PRIVATE PlayerID:STRING
    def __init__(self,InputPlayerID):
        self.__Score=0
        self.__Category="NotQualified"
        self.__PlayerID=InputPlayerID
#Part b
    def GetScore(self):
        return self.__Score
    def Category(self):
        return self.__Category
    def GetPlayerID(self):
        return self.__PlayerID
#Part c
    def SetPlayerID(self):
        flag=False
        while flag==False:
            userinp=input("Enter appropirate playerId:")
            if len(userinp)<=15 and len(userinp)>=4:
                flag=True
            else:
                flag=False
        if flag==True:
            self.__PlayerID=userinp
#Part d
    def SetScore(self,ScoreInput):
        if ScoreInput>=0 and ScoreInput<=150:
            self.__Score=ScoreInput
            return True
        else:
            print("Invalid Score")
            return False
#Part e
    def SetCategory(self):
        if self.__Score>120:
            self.__Category="Advanced"
        elif self.__Score>80 and self.__Score<=120:
            self.__Category="Intermediate"
        elif self.__Score>=50 and self.__Score<=100:
            self.__Category="Beginner"
        else:
            self.__Category="Not Qualified"
#Part f
def CreatePlayer():
    userid=input("Enter Your Appropirate ID:")
    userscore=input("Enter Your Appropirate Score:")
    JoannePlayer=Player(userid)
    if JoannePlayer.SetScore()==False:
        print("Invalid Score")
    else:
        temp=JoannePlayer.SetCategory()
    print(temp)


#Q11 Part a 
class ExaminationPaper():
    #PRIVATE FinalMark:STRING
    #PRIVATE Grade:STRING
    #PRIVATE PaperID:STRING
    def __init__(self,centrenumber,candidatenumber):
        self.__FinalMark=0
        self.__Grade="Fail"
        self.__PaperID=centrenumber+candidatenumber
#Part b 
    def GetFinalMark(self):
        return self.__FinalMark
    def GetGrade(self):
        return self.__Grade
    def GetPaperID(self):
        return self.__PaperID
#Part c
    def SetFinalMark(self,Mark):
        if int(Mark)>=0 and int(Mark)<=90:
            self.__FinalMark=Mark
            return True
        else:
            return False
#Part d
    def SetGrade(self,DistMark,MeritMark,PassMark):
        if self.__FinalMark>=DistMark:
            self.__Grade="Distinction"
        elif self.__FinalMark>="MeritMark":
            self.__Grade="Merit"
        elif self.__FinalMark>="PassMark":
            self.__Grade="Pass"
        else:
            self.__Grade="Fail"
#Part e
def Main():
    usercn=input("Enter Your Centre Number:")
    usercan=input("Enter Your Candidate Number:")
    usermark=input("Enter Your Marks:")
    ThisPaper=ExaminationPaper(usercn,usercan)
    if ThisPaper.SetFinalMark()==False:
        print("Invalid Marks:")
    else:
        temp1=ThisPaper.SetGrade()
        print(temp1)
         


#Q12 Part a
class Cards():
    #PRIVATE Number:INTEGER
    #PRIVATE Shape:STRING
    def __init__(self,Number,Shape):
        if Number>0 and Number<9:
            if Shape=="square" or "triangle" or "circle":
                self.__Number=Number
                self.__Shape=Shape
        else:
            print("Error")
#Part e (for some reason the examiner for smoking crack)
    def comapre(self,card1,card2):
     if card1.GetNumber()==card2.GetNumber() and card1.GetShape()==card2.GetShape():
        print("SNAP")
        return -1
     elif card1.GetNumber()>card2.GetNumber():
        return card2.GetNumber
     else:
        return card2.GetNumber()
#Part b
    def GetNumber(self):
        return self.__Number
    def GetShape(self):
        return self.__Shape
#Part c
OneS=Cards(1,"square")
#Q8 Part a
class Employee():
    #PRIVATE EmployeeID:STRING
    #PRIVATE Name:STRING
    #PRIVATE Address:STRING
    #PRIVATE DateOfBirth:Date
    def __init__(self,EmployeeID,Name,Address,DateOfBirth):
        self.__EmployeeID=EmployeeID
        self.__Name=Name
        self.__Address=Address
        self.__DateOfBirth=DateOfBirth
#Part b
    def GetEmployeeID(self):
        return self.__EmployeeID
#Part c 
    def SetEmployeeID(self,newid):
        self.__EmployeeID=newid
#Part d
class SalaryEmployee(Employee):
    def __init__(self,EmployeeID,Name,Address,DateOfBirth,MonthlyPayment,HoursThisMonth,PublicHoliday,Pension):
        super().__init__(EmployeeID,Name,Address,DateOfBirth)
        self.__MonthlyPayment=MonthlyPayment
        self.__HoursThisMonth=HoursThisMonth
        self.__PublicHoliday=PublicHoliday
        self.__Pension=Pension
    def SetPension(self,newval):
        if newval==True or newval==False:
            self.__Pension=newval
            return True
        else:
            return False
    #def CalculateMonthlySalary(self,SalaryEmployee):
        #temp2=int(self.__MonthlyPayment/SalaryEmployee.BonusPayment)
        #temp3=int(self.__MonthlyPayment/SalaryEmployee.PensionPayment)
        #print(temp3)
        #print(temp2)
        #temp4=(int(self.__MonthlyPayment+temp2-temp3))
        #print(temp4)
#Q9 Part a
class PrintAccount():
    #PRIVATE FirstName:STRING
    #PRIVATE LastName:STRING
    #PRIVATE PrintID:STRING
    #PRIVATE Credits:INTEGER
    def __init__(self,FN,LN,PD,CS):
        self.__FirstName=FN
        self.__LastName=LN
        self.__PrintID=PD
        self.__Credits=50
        self.__StudentAccounts=[]*999
#Part b
    def GetPrintID(self):
        return self.__PrintID
    def SetFirstName(self,newfs):
        self.__FirstName=newfs
    def SetLastName(self,newls):
        self.__LastName=newls
    def SetPrintID(self,newpd):
        self.__PrintID=newpd
#Part c
    def GetName(self):
        return self.SetFirstName, " ",self.SetLastName
    def AddCredits(self,MoneyInput):
        if MoneyInput>=20:
            temp1=MoneyInput+self.__Credits
        elif MoneyInput>=10 and MoneyInput<=19:
            temp2=MoneyInput+(self.__Credits-25)
        else:
            temp3=MoneyInput
#Part d
#DECLARE StudentsAccounts ARRRY[0:1000] OF:PrintAccountant










#Q6 Part a
class Lesson():
    def __init__(self,LessonType,Instructor):
        self.__LessonType=LessonType
        self.__Instructor=Instructor
#Part b
    def GetLessonType(self):
        return self.__LessonType
    def GetInstructor(self):
        return self.__Instructor
#Part c
    def GetFee(self,SkillLevel):
        if SkillLevel=="B":
            return 45
        elif SkillLevel=="I":
            return 50
        elif SkillLevel=="A":
            return 55
        else:
            return -1
#Part d
#DECLARE LessonObject ARRAY [0:9] OF LESSON
LessonObject=[]*9
#Part e
LessonObject[2]=Lesson("Improve Your Serve")


#Q7
import random
class Character():
    def __init__(self,Name):
        self.__Name=Name
        self.__Skill=0
        self.__Health=50
        self.__Shield=random.randint(1,25)
#Part b
    def GetName(self):
        return self.__Name
    def GetSkill(self,newskill):
        if newskill>=10 and newskill<=25:
            self.__Skill=self.__Skill+newskill
            if self.__Skill+newskill>=200:
                newskill=200
                return 0
            else:
                return 1
        else:
            return -1
#Part c
    #DECLARE CharacterArray ARRAY [0:5] OF Character
CharacterArray=[]*5
#part d
CharacterArray[0]=Character("Victory")

#Q14 Part a
class GameElement():
    def __init__(self,PosX,PosY,Wid,Hei,IFN):
        self.__PositionX=PosX
        self.__PositionY=PosY
        self.__Width=Wid
        self.__Height=Hei
        self.__ImageFilename=IFN
    def GetDetails(self):
        return self.__PositionX+self.__PositionY+self.__Width+self.__Height+self.__ImageFilename
#Part b
class Scenery(GameElement):
    def __init__(self,PosX,PosY,Wid,Hei,IFN,causedamage,damagepoints):
        super().__init__(PosX,PosY,Wid,Hei,IFN)
        self.__CauseDamage=causedamage
        self.__DamagePoints=damagepoints
    def GiveDamagePoints(self):
        if self.__CauseDamage==True:
            return self.__DamagePoints
#Part d
    #def GetScenery(self):
        #Message=GetDetails(self)
        #Message=Message+"Causes Damage:",self.__CauseDamage,"DamagePoints:",self.__DamagePoints
        #return Message


#Part c
GiftBox=Scenery(150,150,50,75,"box.png",True,50)


#Q15 Part a
class Member():
    def __init__(self,FirstName,LastName,DateOfBirth,Gender):
        self.__FirstName=FirstName
        self.__LastName=LastName
        self.__DateOfBirth=DateOfBirth
        self.__Gender=Gender
    def Intoduction(self):
        return "Hello,I am ",self.__FirstName, " ",self.__LastName
    def DisplayFullNameAndDateOfBirth(self):
        print(self.__FirstName,self.__LastName,self.__DateOfBirth)

#Part b
class Competitor(Member):
    def __init__(self,FirstName,LastName,DateOfBirth,Gender,Sport):
        super().__init__(FirstName,LastName,DateOfBirth,Gender)
        self.__Sport=Sport
    def DisplayFullNameAndDateOfBirth(self):
        print(self.__FirstName,self.__LastName,self.__DateOfBirth)
BMXJudge=Competitor("Omar","Ellaboudy","17/03/1993","Male",True,"Judge")


#Q17 Part a
class Account():
    def __init__(self,AccountNumber,Balance):
        self.__AccountNumber=AccountNumber
        self.__Balance=Balance
    def GetAccountNumber(self):
        return self.__AccountNumber
    def GetBalance(self):
        return self.__Balance
#Part b
class SavingAccounts(Account):
    def __init__(self,AccountNumber,Balance,PayInt,AmountP):
        super().__init__(AccountNumber,Balance)
        self.__PayInt=PayInt
        self.__AmountP=AmountP


#Q22 Part a
class StockItem():
    def __init__(self):
        self.__Title=""
        self.__DateAquired=""
        self.__OnLoan=False
    def ShowTitle():
        pass
    def ShowDateAquired():
        pass
    def ShowOnLoan():
        pass
#Part b
class Book(StockItem):
    def __init__(self):
        self.__Author=""
        self.__ISBN=""
    def ShowAuthor():
        pass
    def ShowISBN():
        pass
#Part c
NewBook=Book("Computer","A.Nyone","09911","12/11/2001",False)


            





    






                
                





    
    
    
    











            

        
    
     



            



        




    

