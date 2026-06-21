class Vehicle():
    # PRIVATE ID : STRING
    # PRIVATE MaxSpeed : INTEGER
    # PRIVATE CurrentSpeed : INTEGER
    # PRIVATE IncreaseAmount : INTEGER
    # PRIVATE HorizontalPosition : INTEGER
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP):
        self.__ID = IDP
        self.__MaxSpeed = MaxSpeedP
        self.__IncreaseAmount = IncreaseAmountP
        self.__CurrentSpeed = 0
        self.__HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def SetCurrentSpeed(self, CurrentSpeedNew):
        self.__CurrentSpeed = CurrentSpeedNew

    def SetHorizontalPosition(self, HorizontalPositionNew):
        self.__HorizontalPosition = HorizontalPositionNew

    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed

        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed

    def Outputprocedure(self):
        print("Current Speed: ", self.__CurrentSpeed)
        print("Horizontal Position", self.__HorizontalPosition)




class Helicopter(Vehicle):
    # PRIVATE VerticalPosition : INTEGER
    # PRIVATE VerticalChange : INTEGER
    # PRIVATE MaxHeight : INTEGER
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP, VerticalChangeP, MaxHeightP):
        super().__init__(IDP, MaxSpeedP, IncreaseAmountP)
        self.__VerticalChange = VerticalChangeP
        self.__MaxHeight = MaxHeightP
        self.__VerticalPosition = 0

    def IncreaseSpeed(self):
        self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        super().IncreaseSpeed()

    def Outputprocedure(self):
        super().Outputprocedure()
        print("Veritcal Position: ", self.__VerticalPosition)


Car = Vehicle("Tiger", 100, 20)
Helicop = Helicopter("Lion", 350, 40, 3, 100)

Car.IncreaseSpeed()
Car.IncreaseSpeed()
Car.Outputprocedure()

Helicop.IncreaseSpeed()
Helicop.IncreaseSpeed()
Helicop.Outputprocedure()


























