#Part a
#DECLARE StackData:ARRAY[0:9]OF INTEGER
global StackData
global StackPointer
StackData=[0]*10
StackPointer=0
#Part b
def Output():
    global StackData
    global StackPointer
    for x in range(10):
        print(StackData[x])
    print(StackPointer)
#Part c
def Push(DataToPush):
    global StackData
    global StackPointer
    if StackPointer==10:
        return False
    else:
        StackData[StackPointer]=DataToPush
        StackPointer=StackPointer+1
        return True
#Part di
for x in range(11):
    userinp=int(input("Enter 11 numbers:"))
    Temp=Push(userinp)
    if Temp==False:
        print("Not Added")
    else:
        print("Added")
print(StackData)
#Part dii
#Part ei
def Pop():
    global StackData
    global StackPointer
    if StackPointer==0:
        return -1
    else:
        DataToReturn=StackData[StackPointer]
        StackPointer=StackPointer-1
        return DataToReturn
#Part eii
Pop()
Pop()
print(StackData)
