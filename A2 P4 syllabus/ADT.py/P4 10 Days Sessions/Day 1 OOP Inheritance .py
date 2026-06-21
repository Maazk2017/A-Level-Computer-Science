class Vehicle():
#Part a
    # PRIVATE ID : STRING
    # PRIVATE MaxSpeed : INTEGER
    # PRIVATE CurrentSpeed : INTEGER
    # PRIVATE IncreaseAmount : INTEGER
    # PRIVATE HorizontalPosition : INTEGER
#Part b
    def __init__(self,ID,MaxSpeed,IncreaseAmount):
        self.__ID=ID
        self.__MaxSpeed=MaxSpeed
        self.__IncreaseAmount=IncreaseAmount
        self.__CurrentSpeed=0
        self.__HorizontalPositon=0
#Part c
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    def GetHorizontalPosition(self):
        return self.__HorizontalPositon
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    def SetCurrentSpeed(self,NewCurrentSpeed):
        self.__CurrentSpeed=NewCurrentSpeed
    def SetHorizontalSpeed(self,NewHorizontalPosition):
        self.__HorizontalPositon=NewHorizontalPosition
    
#Part d
    def IncreaseSpeed(self):
        self.__CurrentSpeed=self.__CurrentSpeed+self.__IncreaseAmount
        if self.__CurrentSpeed>self.__MaxSpeed:
            self.__CurrentSpeed=self.__MaxSpeed
        self.__HorizontalPositon=self.__CurrentSpeed
#Part f
    def OutputProcedure(self):
        print("The Horizontal Position is",self.__HorizontalPositon)
        print("The Speed of Vehicle is",self.__CurrentSpeed)
#Part e
class Helicopter(Vehicle):
    def __init__(self,ID,MaxSpeed,IncreaseAmount,VerticalChange,MaximumHeight):
        super().__init__(ID,MaxSpeed,IncreaseAmount)
        self.__VerticalPosition=0
        self.__VerticalChange=VerticalChange
        self.__MaximumHeight=MaximumHeight
    def IncreaseSpeed(self):
        self.__VerticalPosition=self.__VerticalPosition+self.__VerticalChange
        if self.__VerticalPosition>self.__MaximumHeight:
            self.__VerticalPosition=self.__MaximumHeight
        super().IncreaseSpeed()
#Part f
    def OutputProcedure(self):
        print("The Vertical Position is",self.__VerticalPosition)
        super().OutputProcedure()
#Part g
Car=Vehicle("Tiger",100,20)
Helicopter=Helicopter("Lion",350,40,3,100)
Car.IncreaseSpeed()
Car.IncreaseSpeed()
Car.OutputProcedure()

Helicopter.IncreaseSpeed()
Helicopter.IncreaseSpeed()
Helicopter.OutputProcedure()
        
        


    