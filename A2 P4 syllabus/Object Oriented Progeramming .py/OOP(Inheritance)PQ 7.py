#OOP(Inheritance)
#Practice Question
#Q1
#Part A(i)
class character():
    #PRIVATE Name: STRING
    #PRIVATE xposition: INTEGER
    #PRIVATE yposition: INTEGER
    def __init__(self,Name,xposition,yposition):
        self.__Name=Name
        self.__xposition=xposition
        self.__yposition=yposition
#Part (ii)
    def Getxposition(self):
        return self.__xposition
    def Getyposition(self):
        return self.__yposition
#Part(iii)
    def Setxposition(self,newx):
        self.__xposition=self.__xposition+newx
        if self.__xposition>10000:
            self.__xposition=10000
        elif self.__xposition<0:
            self.__xposition=0
    def Setyposition(self,newy):
        self.__yposition=self.__yposition+newy
        if self.__yposition>10000:
            self.__yposition=10000
        elif self.__yposition<0:
            self.__yposition=0
#Part (iv)
    def move(self,direction):
        if direction=="up":
            self.Setyposition(10)
        elif direction=="down":
            self.Setyposition(-10)
        elif direction=="left":
            self.Setxposition(-10)
        else:
            self.Setxposition(10)    
#Part B
Jack=character("Jack",50,50)
#Part C(i)
class Bikecharacter(character):
     #PRIVATE Name: STRING
    #PRIVATE xposition: INTEGER
    #PRIVATE yposition: INTEGER
    def __init__(self,Name,xposition,yposition):
        super().__init__(Name,xposition,yposition)
#Part C(ii)
    def move(self,direction):
        if direction=="up":
            super().Setyposition(20)
        elif direction=="down":
            super().Setyposition(-20)
        elif direction=="left":
            super().Setxposition(-20)
        else:
            super().Setxposition(20)
       
#Part D
Karla=Bikecharacter("Karla",100,50)
#Part E
userchar=input("Choose the Character:")
userdir=(input("Enter the direction:"))
if userchar=="Jack":
    Jack.move(userdir)
    x=Jack.Getxposition()
    y=Jack.Getyposition()
    print("Jack's new position is x =",x,"y =",y)
elif userchar=="Karla":
    Karla.move(userdir)
    x=Karla.Getxposition()
    y=Karla.Getyposition()
    print("Karla's new position is x=",x,"y=",y )


class Character():
    def __init__(self,Name,XPosition,YPosition):
        self.__Name=Name
        self.__XPosition=XPosition
        self.__YPosition=YPosition
    def GetXPosition(self):
        return self.__XPosition
    def GetYposition(self):
        return self.__YPosition
    def SetXPosition(self,val):
        self.__XPosition=self.__XPosition+val
        if self.__XPosition>10000:
            self.__XPosition=10000
        elif self.__XPosition<0:
            self.__XPosition=0
    def SetYPosition(self,val):
        self.__YPosition=self.__YPosition+val
        if self.__YPosition>10000:
            self.__YPosition=10000
        elif self.__YPosition<0:
            self.__YPosition=0
    def move(self,direction):
        if direction=="up":
            self.SetYPosition(10)
        elif direction=="down":
            self.SetYPosition(-10)
        elif direction=="left":
            self.SetXPosition(-10)
        else:
            self.SetXPosition(10)
Jack=Character("Jack",50,50)
class BikeCharacter(Character):
    def __init__(self,Name,XPosition,YPosition):
        super().__init__(Name,XPosition,YPosition)
    def move(self,direction):
        if direction=="up":
            super().SetYPosition(20)
        elif direction=="down":
            super().SetXPosition(-20)
        elif direction=="left":
            super().SetXPosition(-20)
        else:
            super().SetXPosition(20)
Karla=BikeCharacter("Karla",100,50)
userinp1=input("Enter Character Name:")
userinp2=input("Enter the direction:")
if userinp1=="Jack":
    Jack.move(userinp2)
    x=Jack.GetXPosition
    y=Jack.GetYposition
    print("Jack's new position is x=",x,"y=",y )
elif userinp1=="Karla":
    Karla.move(userinp2)
    x=Karla.GetXPosition
    y=Karla.GetYposition
    print("Karla's new position is x=",x,"y=",y )

    


        
        











    
