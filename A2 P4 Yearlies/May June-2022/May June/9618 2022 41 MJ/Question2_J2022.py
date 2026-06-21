#Part a
class Balloon():
    #PRIVATE Health:INTEGER
    #PRIVATE Colour:STRING
    #PRIVATE DefenceItem:STRING
    def __init__(self,DefenceItem,Colour):
        self.__DefenceItem=DefenceItem
        self.__Colour=Colour
        self.__Health=100
#Part b
    def GetDefenceItem(self):
        return self.__DefenceItem
#Part c
    def ChangeHealth(self,newhealth):
        self.__Health=newhealth
#Part d
    def CheckHealth(self):
        if self.__Health<=0:
            return True
        else:
            return False
#Part e
userdef=input("Enter The Defence Item:")
usercol=input("Enter The Colour:")
Balloon1=Balloon(userdef,usercol)
#Part f
def Defend(BalloonObject):
    userstrn=int(input("ENter The Strength:"))
    BalloonObject.ChangeHealth(-userstrn)
    print(BalloonObject.GetDefenceItem())
    temp=BalloonObject.CheckHealth()
    if temp==True:
        print("Health Remaining")
    else:
        print("No Health Remaining")
    return BalloonObject
#Part gi
Defend(Balloon1)
#Part gii