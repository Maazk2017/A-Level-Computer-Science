#Part ai
#DECLARE Queue:ARRAY[0:49]OF STRING
global Queue
global HeadPointer
global TailPointer
Queue=[""]*50
HeadPointer=-1
TailPointer=0
#Part aii
def Enqueue(DataToAdd):
    global Queue
    global TailPointer
    global HeadPointer
    if TailPointer==50:
        print("Queue is Full")
    else:
        Queue[TailPointer]=DataToAdd
        TailPointer=TailPointer+1
        if HeadPointer==-1:
            HeadPointer=0
#Part aiii
def Dequeue():
    global Queue
    global HeadPointer
    global TailPointer
    if HeadPointer==-1:
        print("Queue is Empty")
        return "Empty"
    else:
        DataToReturn=Queue[HeadPointer]
        HeadPointer=HeadPointer+1
        if HeadPointer==TailPointer:
            HeadPointer=-1
            TailPointer=0
    return DataToReturn
#Part b
def ReadData():
    try:
        File=open("QueueData.txt","r")
        for line in File:
            LineData=line.strip()
            Enqueue(LineData.strip())
        File.close()
    except IOError:
        print("File Doesn't Exists")
#Part ci
class RecordData():
    #PUBLIC ID:STRING
    #PUBLIC Total:INTEGER
    def __init__(self,ID,Total):
        self.ID=ID
        self.Total=Total
#Part cii
#DECLARE Records:ARRAY[0:49]OF RecordData
#DELCARE NumberOfRecords:INTEGER
global Records
global NumberOfRecords
Records=[]
NumberOfRecords=0
for x in range(50):
    Records.append(RecordData(" ",0))
#Part ciii
def TotalData():
    global Records
    global NumberOfRecords
    DataAccessed=Dequeue()
    Flag=False
    if NumberOfRecords==0:
        Records[NumberOfRecords].ID=DataAccessed
        Records[NumberOfRecords].Total=1
        Flag=True
        NumberOfRecords=NumberOfRecords+1
    else:
        for x in range(0,NumberOfRecords):
            if Records[x].ID==DataAccessed:
                Records[x].Total=Records[x].Total+1
                Flag=True
    if Flag==False:
        Records[NumberOfRecords].ID=DataAccessed
        Records[NumberOfRecords].Total=1
        NumberOfRecords=NumberOfRecords+1
#Part d
def OutputRecords():
    global NumberOfRecords
    for x in range(NumberOfRecords):
        print("ID",Records[x].ID +" "+ "Total",Records[x].Total)
#Part ei
ReadData()
while HeadPointer!=-1:
    TotalData()
OutputRecords()
#Part eii







    

