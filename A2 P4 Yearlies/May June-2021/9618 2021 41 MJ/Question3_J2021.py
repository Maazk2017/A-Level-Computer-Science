#Question 3 Part a
class TreasureChest():
    #PRIVATE question:STRING
    #PRIVATE answer:INTEGER
    #PRIVATE points:INTEGER
    def __init__(self,questionp,answerp,pointsp):
        self.__question=questionp
        self.__answer=answerp
        self.__points=pointsp
#Part ci
    def GetQuestion(self):
        return self.__question
#Part cii
    def CheckAnswer(self,useranswer):
        if useranswer==self.__answer:
            return True
        else:
            return False
#Part ciii
    def getPoints(self,nattempts):
        if nattempts==1:
            return self.__points
        elif nattempts==2:
            return int(self.__points//2)
        elif nattempts==3 or nattempts==4:
            return int(self.__points//4)
        else:
            return 0
arrayTreasure=[]
#DECLARE Part b
def readData():
#DECLARE arrayTreasure:ARRAY [0:14] OF TreasureChest
    try:
        File=open("TreasureChestData.txt","r")
        for x  in range(5): # there are toal 15 lines in the file and questions only 5 so we will iterate 5 times
            questionline=(File.readline().strip())
            answerline=(File.readline().strip())
            pointsline=(File.readline().strip())
            QuestionObject=TreasureChest((questionline),int(answerline),int(pointsline))
            arrayTreasure.append(QuestionObject)
        File.close()
    except IOError:
        print("File doesn't exist")
#Part civ
readData()
userinp=int(input("Enter the question number b/w 1 & 5:"))
attempts=0
Flag=False
question=arrayTreasure[userinp-1].GetQuestion()
print(question)
while Flag==False:
    answer=int(input("Enter correct answer:"))
    temp=arrayTreasure[userinp-1].CheckAnswer(answer)
    if temp==False:
        attempts=attempts+1
    else:
        Flag=True
score=arrayTreasure[userinp-1].getPoints(attempts+1)
print(int(score))
#Part v

    



        
        
            