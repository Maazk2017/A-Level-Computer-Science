#Part a
class Queue():
    #PUBLIC QueueArray:ARRAY [0:99] OF INTEGER
    #PUBLIC HeadPointer:INTEGER
    #PUBLIC TailPointer:INTEGER
    def __init__(self):
        self.QueueArray=[]
        self.HeadPointer=0
        self.TailPointer=0
        for x in range(100):
            self.QueueArray.append(-1)
#Part b
class Queue():
    def __init__(self):
        self.QueueArray=[]
        for x in range(100):
            self.QueueArray.append(-1)
        self.HeadPointer=-1
        self.TailPointer=0
TheQueue=Queue()
#Part c
def Enqueue(AQueue,TheData):
    if AQueue.HeadPointer==-1:
        AQueue.QueueArray[AQueue.TailPointer]=TheData
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
#Part d
def ReturnAllData():
    Temp=""
    for x in range(TheQueue.HeadPointer,TheQueue.TailPointer):
        Temp=Temp+str(TheQueue.QueueArray[x])+" "
    return Temp
#Part ei

for x in range(10):
    Flag=False
    while Flag==False:
        userinp=int(input("Enter 10 Valid Integer Values:"))
        if userinp>=0:
            Temp=Enqueue(TheQueue,userinp)
            if Temp==-1:
                print("Queue is full")
            else:
                print("Added")
            Flag=True
        
IntegerOutput=ReturnAllData()
print(IntegerOutput)
#Part f
def Dequeue(AQueue):
    if AQueue.HeadPointer==-1 or AQueue.HeadPointer==100:
        return -1
    
    else:
        Item=AQueue.QueueArray[AQueue.HeadPointer]
        AQueue.HeadPointer=AQueue.HeadPointer+1
        return AQueue,Item
#Part gi
Value1=Dequeue(TheQueue)
Value2=Dequeue(TheQueue)
if Value1==-1:
    print("Queue Empty")
else:
    print(Value1,"is returned")
if Value2==-1:
    print("Queue Empty")
else:
    print(Value2,"is returned")
print(ReturnAllData())
#Part gii