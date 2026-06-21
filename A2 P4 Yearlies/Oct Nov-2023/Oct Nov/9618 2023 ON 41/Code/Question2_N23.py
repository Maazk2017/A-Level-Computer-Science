# DECLARE Queue : ARRAY[0:49] OF STRING
global Queue
global HeadPointer # int
global TailPointer # int
Queue = [""] * 50
HeadPointer = -1
TailPointer = 0

def Enqueue(Value):
    global Queue
    global HeadPointer
    global TailPointer

    if TailPointer == 50:
        print("The Queue Is Full")
    else:
        Queue[TailPointer] = Value
        TailPointer = TailPointer + 1
        if HeadPointer == -1:
            HeadPointer = 0

def Dequeue():
    global Queue
    global TailPointer
    global HeadPointer

    if HeadPointer == -1:
        print("The Queue Is Empty")
        return "Empty"
    else:
        RemovedItem = Queue[HeadPointer]
        HeadPointer = HeadPointer + 1

    if HeadPointer == TailPointer:
        HeadPointer = -1
        TailPointer = 0
    return RemovedItem


def ReadData():
    try:
        file = open("QueueData.txt", "r")
        for line in file:
            Enqueue(line.strip())
        file.close()
    except IOError:
        print("File Does Not Exist")


class RecordData():
    #PUBLIC ID : STRING
    #PUBLIC Total : INTEGER
    def __init__(self, IDP, TotalP):
        self.ID = IDP
        self.Total = TotalP

#DECLARE Records : ARRAY[0:49] OF RecordData
global Records
global NumberRecords
NumberRecords = 0
Records = []
for x in range(50):
    Records.append(RecordData("", 0))

def TotalData():
    global NumberRecords
    global Records

    DataAccessed = Dequeue()
    Flag = False
    if NumberRecords == 0:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        Flag = True
        NumberRecords = NumberRecords + 1
    else:
        for x in range(0, NumberRecords):
            if Records[x].ID == DataAccessed:
                Records[x].Total = Records[x].Total + 1
                Flag = True

    if Flag == False:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        NumberRecords = NumberRecords + 1


def OutputRecords():
    global NumberRecords
    for x in range(NumberRecords):
        print("ID", Records[x].ID, "Total", Records[x].Total)

ReadData()
while HeadPointer != -1:
    TotalData()
OutputRecords()












