#PRACTICE QUESTION
#Part A
class TreasureChest:
    #PRIVATE question :STRING
    #PRIVATE answer: INTEGER
    #PRIVATE points: INTEGER
    def __init__(self,Que,Ans,Poi):
        self.question=Que
        self.answer=Ans
        self.points=Poi
#Part B(ii)
def getQuestion(self):
    return self.question
def CheckAnswer(self,corrans):
    corrans=int(input("Enter the correct answer:"))
    if corrans==self.answer:
            return False
    else:
            return True
#Part C
def getPoints(self,attempts):
     if attempts==1:
          return self.points
     elif attempts==2:
          Points=int(self.point/2)
          return Points
     elif attempts==3 or attempts==4:
          Points_1=int(self.points/4)
          return Points_1
     else:
          return 0
quiz=TreasureChest("2+2 ?",4,100)

print("Question:",quiz.question())
Flag=True
attempts=0
while Flag==True:
     userinput=int(input("Enter correct answer:"))
     attempts==attempts+1
     checker=quiz.answer(userinput)
     if checker ==True:
          Flag=True

TotalPoints=quiz.points(attempts)
print("Your score is:",TotalPoints)
     


class TreasureChest():
     def __init__(self,qes,ans,poi):
          self.__question=qes
          self.__answer=ans
          self.__points=poi
     def getQuestion(self):
          return self.__question
     def CheckAnswer(self,userans):
          if userans==self.__answer:
               return True
          else:
               return False
     def GetPoints(self,attempts):
          if attempts==1:
               return self.__points
          elif attempts==2:
               return(int((self.__points)/2))
          elif attempts==3 or attempts==4:
               return(int((self.__points)/4))
          else:
               return 0
          


          




     
          


    

     


        



    
    
