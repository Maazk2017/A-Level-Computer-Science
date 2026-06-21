#Part ai
class Vehicle():
    #PRIVATE ID:STRING
    #PRIVATE MaxSpeed:INTEGER
    #PRIVATE CurrentSpeed:INTEGER
    #PRIVATE IncreaseAmount:INTEGER
    #PRIVATE HorizontalPosition:INTEGER
    def __init__(self,ID,MaxSpeed,IncreaseAmount):
        self.__ID=ID
        self.__MaxSpeed=MaxSpeed
        self.__IncreaseAmount=IncreaseAmount
        self.__CurrentSpeed=0
        self.__HorizontalPosition=0
#Part aii
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
#Part aiii
    def SetCurrentSpeed(self,NewSpeed):
        self.__CurrentSpeed=self.__CurrentSpeed+NewSpeed
    def GetHorizontalSpeed(self,NewHSpeed):
        self.__HorizontalPosition=self.__HorizontalPosition+NewHSpeed
#Part aiv
    def IncreaseSpeed(self):
        self.__CurrentSpeed=self.__CurrentSpeed+self.__IncreaseAmount
        if self.__CurrentSpeed>self.__MaxSpeed:
            self.__CurrentSpeed=self.__MaxSpeed
        self.__HorizontalPosition=self.__CurrentSpeed
    def Procedure(self):
        print("The Horizontal Position is",self.__HorizontalPosition)
        print("The speed of vehicle is",self.__CurrentSpeed)
#Part bi
class Helicopter(Vehicle):
    #PRIVATE VetricalPosition:INTEGER
    #PRIVATE VerticalChange:INTEGER
    #PRIVATE MaxHeight:INTEGER
    def __init__(self,ID,MaxSpeed,IncreaseAmount,VerticalChange,MaxHeight):
        super().__init__(ID,MaxSpeed,IncreaseAmount)
        self.__VerticalChange=VerticalChange
        self.__MaxHeight=MaxHeight
        self.__VerticalPosition=0
#Part bii
    def IncreaseSpeed(self):
        self.__VerticalPosition=self.__VerticalChange+self.__VerticalChange
        if self.__VerticalPosition>self.__MaxHeight:
            self.__VerticalPosition=self.__MaxHeight
        super().IncreaseSpeed()
#Part c
    def Procedure(self):
        print("The Vertical Position is",self.__VerticalPosition)
        super().Procedure()
#Part d
car=Vehicle("Tiger",100,20)
helicopter=Helicopter("Lion",350,40,3,100)
car.IncreaseSpeed()
car.IncreaseSpeed()
car.Procedure()

helicopter.IncreaseSpeed()
helicopter.IncreaseSpeed()
helicopter.Procedure()

       


