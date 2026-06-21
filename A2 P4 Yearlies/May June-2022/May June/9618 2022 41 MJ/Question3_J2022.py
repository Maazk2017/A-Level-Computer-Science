#Part a
#DECLARE QueueArray:ARRAY[0:9] OF STRING
#DECLARE headpointer:INTEGER
#DECARE tailpointer:INTEGER
#DECLARE numberofitems:INTEGER
QueueArray=[""]*10
HeadPointer=0
TailPointer=0
NumberOfItems=0

#Part b
def Enqueue(DataToAdd):
    global QueueArray
    global HeadPointer
    global TailPointer
    global NumberOfItems
    if NumberOfItems==10:
        return False
    else:
        QueueArray[TailPointer]=DataToAdd
        if TailPointer>=19:
            TailPointer=0
        else:
            TailPointer=TailPointer+1
    NumberOfItems=NumberOfItems+1
    return True
#Part c
def Dequeue():
    global QueueArray
    global HeadPointer
    global TailPointer
    global NumberOfItems
    if NumberOfItems==0:
        return False
    else:
        ReturnData=QueueArray[HeadPointer]
        HeadPointer=HeadPointer-1
        if HeadPointer>19:
            HeadPointer=HeadPointer+1
    NumberOfItems=NumberOfItems-1
    return ReturnData
#Part di
for x in range(11):
    Value=input("Enter 11 values:")
    temp=Enqueue(Value)
    if temp==False:
        print("Not Successfull")
    else:
        print("Successfull")
ReturnValue1=Dequeue()
ReturnValue2=Dequeue()
print(ReturnValue1)
print(ReturnValue2)
#Part dii


