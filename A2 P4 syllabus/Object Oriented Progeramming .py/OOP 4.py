#Practicse Question
#Q2
#Part 
class Balloon():
        #PRIVATE Health :INTEGER
        #PRIVATE Colour :STRING
        #PRIVATE DefenceItem :STRING
        def __init__(self,Col,Defitem):            
                self.__Colour=Col
                self.__DefenceItem=Defitem
                self.__Health=100            
#Part b
        def GetDefenceItem(self):
         return self.__DefenceItem
#Part c
        def ChangeHealth(self,num):
         self.__Health=self.__Health+num
#Part d
        def CheckHealth(self):
         if self.__Health<=0:
                return True
         else:
            return False
#Part e
#*IMPORTANT
userdefence=input("Enter a Defence Item:")
usercol=input("Enter a colour:")

Balloon_1=Balloon(usercol,userdefence)
#Part f
def Defend(BalloonObject):
       userstr=int(input("Enter opp strength:"))
       # x=x+y
       #x=x-(+y)
       BalloonObject.ChangeHealth(-userstr)
       print("The Defence Item is:",BalloonObject.GetDefenceItem())

       if BalloonObject.CheckHealth()==True:
        print("Health Remaining:")
       else:
        print("No Health Remaining:")

       
       return BalloonObject

#Part g(i)
#*IMPORTANT
Balloon_1=Defend(Balloon_1)

#Part g(ii)
#Run the code with given values

class Balloon():
    def __init__(self,defitem,col):
        self.__DefenceItem=defitem
        self.__Colour=col
        self.__Health=100
    def GetDefenceItem(self):
        return self.__DefenceItem
    def ChangeHealth(self,num):
        self.__Health=self.__Health+num
    def CheckHealth(self):
        if self.__Health<=0:
            return True
        else:
            return False
userinp1=("Enter a DefenceItem:")
userinp2=("Enter a colour:")
Balloon1=Balloon(userinp1,userinp2)
def Defend(BalloonObject):
    userinp3=(int("Enter the strength:"))
    BalloonObject.ChangeHealth(-userinp3)
    print("the efence Item is:",BalloonObject.GetDefenceItem())
    temp=BalloonObject.CheckHealth()
    if temp==True:
        print("No Health Reamining")
    else:
        print("Health Remaining")
    return BalloonObject
Balloon1=Defend(Balloon1)


        

   









  
        


        

       
       
    


                


        
