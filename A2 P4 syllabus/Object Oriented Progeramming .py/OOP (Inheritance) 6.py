#CONCEPT OF INHERITANCE
class PartTimeEmployee():
    #Private Name :STRING
    #PRIVATE Age :INTEGER
    #PRIVATE HourlyRate: INTEGER
    def __init__(self,Name,Age,HR):
        self.__Name=Name
        self.__Age=Age
        self.__HourlyRate=HR
    def GetName(self):
        return self.__Name
    def GetAge(self):
        return self.__Age
    def DailyWage(self,HoursWorked):
        temp=HoursWorked*self.__HourlyRate
        return temp
    
class FullTimeEmployee():
    #Private Name :STRING
    #PRIVATE Age :INTEGER
    #PRIVATE MonthlyRate: INTEGER
    def __init__(self,Name,Age,MR):
        self.__Name=Name
        self.__Age=Age
        self.__MonthlyRate=MR
    def GetName(self):
        return self.__Name
    def GetAge(self):
        return self.__Age
    def YearlySalary(self):
        temp=self.__MonthlyRate*12
        return temp
#INHERITANCE
class Employee():
    #PRIVATE NAME :STRING
    #PRIVATE AGE :INTEGER
    def __init__(self,Name,Age):
        self.__Name=Name
        self.__Age=Age
    def GetName(self):
        return self.__Name
    def GetAge(self):
        return self.__Age
class PartTime(Employee):
    #PRIVATE HourlyRate :INTEGER
    def __init__(self,Name,Age,HourlyRate):
        #Inheritance
        super().__init__(Name,Age)
        self.__HourlyRate=HourlyRate
    def DailyWage(self,HoursWorked):  
        temp=HoursWorked*self.__HourlyRate
        return temp

class FullTime(Employee):
    #PRIVATE MonthlyRate :INTEGER
    def __inint__(self,Name,Age,MonthlyRate):
        super().__init__(Name,Age)
        self.__MonthlyRate=MonthlyRate
        def YearlySalary(self):
            temp1=self.__MonthlyRate*12
            return temp1
        
#parttimeworker=PartTime("Abid",21,5)
#fulltimeworker=FullTime("Asim",23,5000)
#temp2=PartTime.GetName()
#print(Name)

#continued
class vehicle():
    def drive(self):
        print("Driving The Vehicle")  
class car(vehicle):
    # i want to modify my driver function in parent class so it works differently
    def drive(self):
        super().drive()
        print("Driving the car")
#creating an inheritance of the car class
starlet=car()

starlet.drive()

class bike(vehicle):
    def drive(self):
        print("Driving The Bike")
starlet=bike()
starlet.drive()

#Another Example 
class shape():
        def __init__(self,nameofshape):
            self.__nameofshape=nameofshape
        def GetName(self):
            return self.__nameofshape
        def area(self):   
         print("Welcome To Area Calculator")
         print("Area is")
class circle(shape):
    #PRIVATE radius :INTEGER
    def __init__(self,nameofshape,radius):
        super().__init__(nameofshape)
        self.__radius=radius
    def area(self):
        super().area()
        temp=int(3.14*self.__radius*self.__radius)
        print(temp)
#creating an inheritance of the car class
mycircle=circle("Pappo shape",6)
mycircle.area()
temp=mycircle.GetName()
print(temp)



