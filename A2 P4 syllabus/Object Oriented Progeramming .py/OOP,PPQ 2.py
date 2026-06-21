#Q19 Part a
class SafetyDepositBox():
    def __init__(self):
        self.__Code=""
        self.__State="Open-NoCode"
#Part b
    def Reset(self):
        self.__Code=""
    def SetState(self,newstate):
        self.__State=newstate
        print(self.__State)
    def SetNewCode(self,newcode):
        self.__Code=newcode
        print("The New Code is:",self.__Code)
#Part c
    def Valid(self,s):
        digits=("0","1","2","3","4","5","6","7","8","9")
        isvalid =False
        if (len(s))==4:
            if (s[0]in digits) and (s[1]in digits) and (s[2]in digits) and (s[3]in digits):
                isvalid=True
        return(isvalid)
#Part d
    def StateChange(self):
        chars=input("Enter characters:")
        if chars=="R":
            if self.__State=="Open-CodeSet":
                self.Reset()
        elif chars==self.__Code:
            if self.__State=="Locked":
                self.SetState("Open-CodeSet")
            elif self.__State=="Closed":
                self.SetState("Locked")
        elif chars==""and self.__State=="Open-CodeSet":
            self.SetState("Closed")
        elif self.Valid(chars):
            if self.__State=="Open-NoCode":
                self.SetNewCode(chars)
            else:
                print("Error-does not match setcode")
        else:
            print("Error-Code format incorrect")
#Part e
def Main():
    ThisSafe=SafetyDepositBox()
    while True:
        ThisSafe.StateChange
#Q20 part a
class TicketMachine():
    def __init__(self):
        self.__Amount=0
        self.__State="Idle"
#Part b
    def SetState(self,newstate):
        self.__State=newstate
        print(self.__State)
    def ReturnCoins(self):
        print(self.__Amount)
        self.__Amount=0
    def ValidCoin(self,s):
        digit=("10","20","50","100")
        if s=="10" or s=="20" or s=="50" or s=="100":
            isvalid=True
        else:
            isvalid=False
        return(isvalid)
    def PrintTicket(self):
        print("ticket")
        self.__Amount=0
#Part c
    def CoinInserted(self,coin):
        temp1=int(coin)
        self.__Amount=self.__Amount+temp1
#Part d
    def StateChnage(self):
        newinput=input()
        if newinput=="C":
            if self.__State=="Counting":
                self.SetState("Cancelled")
                self.ReturnCoins()
                self.SetState("Idle")
        elif newinput=="A":
            if self.__Amount==0:
                print("No Coins inserted")
                self.SetState("Idle")
            else:
                self.SetState("Accepted")
                self.PrintTicket()
                self.SetState("Idle")
        elif self.ValidCoin(newinput):
            self.CoinInserted(newinput)
            self.SetState("Counting")
        else:
            print("Error-not a valid coin")
#Part e
def Main():
    ParkingMeter=TicketMachine()
    while True:
        ParkingMeter.SetState()

#Q23 Part a
class Student():
    def __init__(self):
        self.__StudentName=""
        self.__DateOfBirth=""
    def ShowStudentName():
        pass
    def ShowDateOfBirth(self):
        pass
class FullTimeStudent(Student):
    def __init__(self):
        self.__Address=""
        self.__TelephoneNumber=""
    def ShowAddress(self):
        pass
    def ShowTelephoneNumber():
        pass
NewStudent=FullTimeStudent("A.Nyone","12/11/1990","099111")

#Q16 Part a
class Desert():
    def __init__(self,Grid,StepCounter,AnimalList,NumberOfAnimals):
        self.__Grid=Grid
        self.__StepCounter=StepCounter
        self.__AnimalList=AnimalList
        self.__NumberOfAniamls=NumberOfAnimals
#Part b

    



        





        
        
        
            
