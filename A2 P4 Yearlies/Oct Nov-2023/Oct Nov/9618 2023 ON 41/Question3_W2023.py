#Part ai
class Character():
    #PRIVATE Name:STRING
    #PRIVATE XPosition:INTEGER
    #PRIVATE YPosition:INTEGER
    def __init__(self,Name,XPosition,YPosition):
        self.__Name=Name
        self.__XPosition=XPosition
        self.__YPosition=YPosition
#Part aii
    def GetXPosition(self):
        return self.__XPosition
    def GetYPosition(self):
        return self.__YPosition
#Part aiii
    def SetXPosition(self,NewXPos):
        if NewXPos <0:
            NewXPos=0
        elif NewXPos>10000:
            NewXPos=10000
    def SetYPosition(self,NewYPos):
        if NewYPos<0:
            NewYPos=0
        elif NewYPos>10000:
            NewYPos=10000
#Part aiv
    def Move(self,Direction):
        if Direction=="up":
            self.__YPosition=self.__YPosition+10
        elif Direction=="down":
            self.__YPosition=self.__YPosition-10
        elif Direction=="left":
            self.__XPosition=self.__XPosition-10
        else:
            self.__XPosition=self.__XPosition+10
#Part b
Jack=Character("Jack",50,50)
#Part ci
class BikeCharacter(Character):
    def __init__(self,Name,XPosition,YPosition):
        super().__init__(Name,XPosition,YPosition)
#Part cii
    def Move(self,Direction):
        if Direction=="up":
            super().SetYPosition(super().GetYPosition()+20)
        elif Direction == "down":
            super().SetYPosition(super().GetYPosition() - 20)
        elif Direction == "left":
            super().SetXPosition(super().GetXPosition() - 20)
        elif Direction == "right":
            super().SetXPosition(super().GetXPosition() + 20)
#Part d
Karla=BikeCharacter("Karla",100,50)
#Part ei
userchr=input("Enter the character you want:")
userdir=(input("Enter the direction you want to move:"))
if userchr=="Jack":
    Jack.Move(userdir)
    x=Jack.GetXPosition()
    y=Jack.GetXPosition()
    print("Jack's new position is X=",x,"y=",y)
else:
    Karla.Move(userdir)
    x=Karla.GetXPosition()
    y=Karla.GetYPosition()
    print("Karla's new position is X=",x,"y=",y)
#Part eii
