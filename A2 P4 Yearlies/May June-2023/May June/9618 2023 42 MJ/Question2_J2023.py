#Part a
class SaleData():
    #PUBLIC ID:STRING
    #PUBLIC Quantity:INTEGER
    def __init__(self,ID,Quantity):
        self.ID=ID
        self.Quantity=Quantity
#Part b
#DELCARE CircularQueue:ARRAY[0:4]OF SaleData
#DECLARE HeadPointer:INTEGER
#DECLARE TailPointer:INTEGER
#DECLARE NumberOfItems:INTEGER
global CircularQueue
global HeadPointer
global TailPointer
global NumberOfItems
CircularQueue=[]
for i in range(5):
    CircularQueue.append(SaleData("",1))
print(CircularQueue)
HeadPointer=0
TailPointer=0
NumberOfItems=0
#Part c
def Enqueue(Record):
    global CircularQueue
    global TailPointer
    global NumberOfItems
    if NumberOfItems==5:
        return -1
    else:
        CircularQueue[TailPointer]=Record
    if TailPointer==4:
        TailPointer=0
    else:
        TailPointer=TailPointer+1
    NumberOfItems=NumberOfItems+1
    return 1
#Part d
def Dequeue():
    global CircularQueue
    global NumberOfItems
    global HeadPointer
    if NumberOfItems==0:
        return SaleData("",-1)
    else:
        ReturnData=CircularQueue[HeadPointer]
        HeadPointer=HeadPointer+1
    if HeadPointer>4:
        HeadPointer=0
    NumberOfItems=NumberOfItems-1
    return ReturnData
#Part e
def EnterRecord():
    userid=input("Enter The Id:")
    userquantity=int(input("Enter The Quantity:"))
    SaleRecord=SaleData(userid,userquantity)
    Temp=Enqueue(SaleRecord)
    if Temp==-1:
        print("Full")
    else:
        print("Stored")
#Part fi
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
Temp=Dequeue()
if Temp.ID=="":
    print("Queue is empty")
else:
    print(Temp.ID +" "+ str(Temp.Quantity))
EnterRecord()
for x in range(5):
    Records=CircularQueue[x]
    print(Records.ID +" "+ str((Records.Quantity)))
#Part fii



