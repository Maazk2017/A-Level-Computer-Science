#ADT ALL QUEUE PPQ QUESTIONS
#Question 3a
#Queue
queuearray=[""]*10
numberofitems=0
headpointer=0
tailpointer=0
#b
def enqueue(datatoadd):
    global numberofitems
    global headpointer
    global tailpointer
    if numberofitems==10:
        return False
    queuearray[tailpointer]=datatoadd
    if tailpointer>=9:
        tailpointer=0
    else:
        tailpointer=tailpointer+1
    numberofitems=numberofitems+1
    return True
#c
def dequeue():
    global numberofitems
    global headpointer
    global tailpointer
    if headpointer==0:
        return "False"
    else:
      temp=queuearray[headpointer]
      headpointer=headpointer+1
    if headpointer>9:
        headpointer=0
    numberofitems=numberofitems-1
    return temp
#d
for i in range(11):
    userinp=input("Enter 10 values")
    enqueue(userinp)
    if enqueue==True:
        print("Successful")
    else:
        print("Unseccessful")
value1=dequeue()
print(value1)
value2=dequeue()
print(value2)
#Question 6a
#Queue
#DECLARE Queue ARRAY [0:99] OF INTEGERS
Queue=[0]*100
HeadPointer=-1
TailPointer=0
#b
def Enqueue(val):
    global Queue
    global HeadPointer
    global TailPointer
    if TailPointer<100:
        Queue[TailPointer]=val
        TailPointer=TailPointer+1
        if HeadPointer==-1:
            HeadPointer=0
            return True
    else:
        return False
#c
for i in range(1,21):
    Temp=Enqueue(i)
    if Temp==True:
        print("Successful")
    else:
        print("Unseccessful")
#d
def RecursiveOutput(Start):
    if Start==0:
        return Queue[Start]
    else:
        return Queue[Start]+RecursiveOutput((Start-1))
#e
print(str(RecursiveOutput(TailPointer-1)))
#Question 8a
#Queue #21 #77
class SaleData:
    def __init__(self,SaleIDp,Quantityp):
        self.SaleID=SaleIDp
        self.Quantity=Quantityp
#b
#DECLARE CircularQueue ARRAY [0:4] OF SaleData
CircularQueue=[]
TailPointer=0
HeadPointer=0
NumberOfItems=0
for x in range(5):
    CircularQueue.append((SaleData("",-1)))
#c
def Enqueue(RecordToAdd):
    global CircularQueue
    global TailPointer
    global headpointer
    global NumberOfItems
    if CircularQueue==5:
        return -1
    CircularQueue[TailPointer]=RecordToAdd
    if TailPointer>=4: #or TailPointer==4
        TailPointer=0
    else:
        TailPointer=TailPointer+1
    NumberOfItems=NumberOfItems+1
    return 1
#d
def Dequeue():
    global CircularQueue
    global HeadPointer
    global NumberOfItems
    RecordRemoved=SaleData("",-1)
    if not(NumberOfItems==0):
        RecordRemoved=CircularQueue[HeadPointer]
        NumberOfItems=NumberOfItems-1
    if HeadPointer==4:
        HeadPointer=0
    else:
        HeadPointer=HeadPointer+1
    return RecordRemoved
#e
def EnterRecord():
    inputid=input("Enter Sale ID:")
    inputqunatity=int(input("Enter The Quantity:"))
    Record=SaleData(inputid,inputqunatity)
    temp=Enqueue(Record)
    if temp==-1:
        print("Full")
    else:
        print("Stored")
#f
for i in range(6):
    EnterRecord()
returnvalue=Dequeue()
if returnvalue.SaleID=="":
    print("No Items")
else:
    print(returnvalue.SaleID," ",returnvalue.Quantity)
EnterRecord()
for z in range(5):
    print(CircularQueue[z].SaleID," ",CircularQueue[z].Quantity)
#Question 9a 23,84
#QUEUE 
#DECLARE Queue ARRAY [0:49] OF STRING
Queue=[""]*50
HeadPointer=-1
TailPointer=0
#b
def Enqueue(text):
    global Queue
    global HeadPointer
    global TailPointer
    if TailPointer<50:
        Queue[TailPointer]=text
        TailPointer=TailPointer+1
        if HeadPointer==-1:
            HeadPointer=0
    else:
        print("Queue Is Full")
#c
def Dequeue():
    global Queue
    global HeadPointer
    global TailPointer
    if HeadPointer==-1 or HeadPointer==TailPointer:
        print("Queue Is Empty")
        return "Empty"
    else:
        previoustext=Queue[HeadPointer]
        HeadPointer=HeadPointer+1
        return previoustext
#d
def ReadData():
    try:
        file=open("QueueData.txt","r")
        for line in file:
            Enqueue(line.strip())
        file.close()
    except IOError:
        print("File Does'nt Exists or Incorrect File Name")
#e
class RecordData():
    #PRIVATE self.__ID:STRING
    #PRIVATE self.__Total:STRING
    def __init__(self,IDp,Totalp):
        self._ID=IDp
        self._Total=Totalp
    def GetID(self):
        return self._ID
    def GetTotal(self):
        return self._Total
    def SetTotal(self,newtotal):
        self._Total=newtotal
#f 
#DECLARE Records ARRAY[0:49] OF RecordData
Records=[""]*50
NumberRecords=0
#g
#def TotalData():
 #   global Records
 #   global NumberRecords
 #   Flag=False
 #   DataAccessed=Dequeue()
 #   if NumberRecords==0:
 #       Records[NumberRecords].ID=DataAccessed
 #       Records[NumberRecords].Total=1
 #       Flag=True
 #       NumberRecords=NumberRecords+1
 #   else:
 #       for x in range(0,NumberRecords):
 #           if Records[x].GetID()==DataAccessed:
  #              Records[x].SetTotal(Records[x].GetTotal()+1)
 #               Flag=True
 #   if Flag==False:
 #       Records[NumberRecords].ID=DataAccessed
 #       Records[NumberRecords].Total=1
#        NumberRecords=NumberRecords+1
#def OutputRecords():
#   for x in range(0,NumberRecords):
#       print("ID",Records[x].GetID(),"Total",Records[x].GetTotal())
#h
#ReadData()
#TotalData()
#OutputRecords()


#Question 11a 30 93
#Queue
#DECLARE QueueData ARRAY [0:19] OF STRING
QueueData=[""]*20
QueueHead=-1
QueueTail=-1
#b
def Enqueue(DataToAdd):
    global Queue
    global QueueHead
    global QueueTail
    if QueueTail==19:
        return False
    elif QueueHead==-1:
        QueueHead=0
    QueueTail=QueueTail+1
    QueueData[QueueTail]=DataToAdd
    return True
 
#c
def Dequeue():
    if HeadPointer==-1 or QueueHead>20 or QueueHead>QueueTail:
        return "false"
    else:
        DataToReturn=QueueData[QueueHead]
        QueueHead=QueueHead+1
        return DataToReturn
#d
#Difficult Question will complete later





#Question 14a
#Queue 
class Queue:
    def __init__(self):
        self.QueueArray=[]
        HeadPointer=0
        TailPointer=0
        for x in range(100):
            self.__QueueArray.append[-1]
#b
class Queue:
    def __init__(self):
        self.QueueArray=[]
        self.HeadPointer=-1
        self.TailPointer=0
        for x in range(100):
            self.QueueArray.append[-1]
TheQueue=Queue()
#c  
def Enqueue(AQueue,TheData):
    if AQueue.HeadPointer==-1:
        AQueue.QueueArray[AQueue.Tailpointer]=TheData
        AQueue.HeadPointer=0
        AQueue.TailPointer=AQueue.TailPointer+1
        return 1
    else:
        if AQueue.TailPointer>99:
            return -1
        else:
            AQueue.QueueArray[AQueue.TailPointer]=TheData
            AQueue.TailPointer=AQueue.TailPointer+1
            return 1
#d
def ReturnAllData(TheQueue):
    temp=""
    for x in range(TheQueue.HeadPoointer,TheQueue.TailPointer):
        temp=temp+str(TheQueue.QueueArray[x])+" "
    return temp
#e

    
    

    




        



        
    
