#Part a
#DELCARE Queue:ARRAY[0:99]OF INTEGERS
#DECALARE HeadPointer:INTEGER
#DECLARE TailPointer:INTEGER
global HeadPointer
global TailPointer
Queue=[0]*100
HeadPointer=-1
TailPointer=0
#Part b
def Enqueue(DataToAdd):
    global Queue
    global TailPointer
    global HeadPointer
    if TailPointer<100:
        Queue[TailPointer]=DataToAdd
        TailPointer=TailPointer+1
        if HeadPointer==-1:
            HeadPointer=0
            return True
    else:
        return False
#Part c
FinalFlag=False
for x in range(21):
    Temp=Enqueue(x)
    if Temp==False:
        FinalFlag=True
if FinalFlag==False:
    print("Successfull")
else:
    print("Unsuccessfull")
#Part d
def RecursiveOutput(Start):
    if Start<0:
        return 0
    else:
        return Queue[Start]+RecursiveOutput(Start-1)
#Part ei
Value=RecursiveOutput(TailPointer)
print(Value)
#Part eii
