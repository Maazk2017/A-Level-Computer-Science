#Part ai
class Employee():
    #PRIVATE HourlyPay:REAL
    #PRIVATE EmloyeeNumber:STRING
    #PRIVATE JobTitle:STRING
    #PRIVATE PayYear2022:ARRAY[0:51]OF REAL
    def __init__(self,HourlyPay,EmployeeNumber,JobTitle):
        self.__HourlyPay=HourlyPay
        self.__EmployeeNumber=EmployeeNumber
        self.__JobTitle=JobTitle
        self.__PayYear2022=[0.0]*52
#Part ii
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
#Part iii
    def SetPay(self,weeknumber,hoursworked):
        Pay=float(self.__HourlyPay)*hoursworked
        self.__PayYear2022[weeknumber-1]=Pay
#Part iv
    def GetTotalPay(self):
        Total=0
        for x in range(len(self.__PayYear2022)):
            Sum=self.__PayYear2022[x]
            Total=Total+Sum
        return Total
#Part bi
class Manager(Employee):
    #PRIVATE BonusValue:REAL
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle, BonusValue ):
        super().__init__(HourlyPay, EmployeeNumber, JobTitle)
        self.__BonusValue=BonusValue
#Part bii
    def SetPay(self,weeknumber,hoursworked):
        TotalPay=hoursworked+(hoursworked*(self.__BonusValue/100))
        super().SetPay(weeknumber,hoursworked)
#Part c
#DECLARE EmployeeArray[0:7]OF Employee
EmployeeArray = [Employee(0.0, "", "")] * 8

MaybeBonus=""
JobTitle=""
try:
    EmployeeFile=open("Employees.txt","r")
    for x in range(8):
        hourlypay=float(EmployeeFile.readline().strip())
        employeenumber=EmployeeFile.readline().strip()
        MaybeBonus=EmployeeFile.readline().strip()
        try:
            Bonus=float(MaybeBonus)
            JobTitle=EmployeeFile.readline().strip()
            EmployeeArray[x]=Manager(hourlypay,employeenumber,JobTitle,Bonus)
        except:
            JobTitle==MaybeBonus
            EmployeeArray[x]=Employee(hourlypay,employeenumber,JobTitle)
    EmployeeFile.close()
except IOError:
    print("File not found")
#Part d
def EnterHours():
    try:
        File=open("HoursWeek1.txt","r")
        for x in range(8):
            employeenumber=File.readline().strip()
            hoursworked=float(File.readline().strip())
            for y in range(8):
                if EmployeeArray[y].GetEmployeeNumber() == employeenumber:
                    EmployeeArray[y].SetPay(1, hoursworked)
        File.close()
    except IOError:
        print("File not found")
#Part ei
EnterHours()
for x in range(8):
    print(EmployeeArray[x].GetEmployeeNumber(),str(EmployeeArray[x].GetTotalPay()))
#Part eii

            
      


    



