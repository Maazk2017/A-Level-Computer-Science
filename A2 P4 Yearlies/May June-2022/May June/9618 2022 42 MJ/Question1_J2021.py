#Part a
#DECLARE StackData:ARRAY[0:10] OF INTEGER
#DECLARE StackPointer:INTEGER
StackData=[0]*10
StackPointer=0
#Part b
def Output():
    for x in range(len(StackData)):
        print(StackData[x])
    print(StackPointer)
#Part c
def Push(DataToPush):
    global StackData
    global StackPointer
    if StackPointer>9:
        return False
    else:
        StackData[StackPointer]=DataToPush
        StackPointer=StackPointer+1
        return True
#Part dii
#Paet ei
def Pop():
    global StackData
    global StackPointer
    if StackData==0:
        return -1
    else:
        StackPointer=StackPointer-1
        ReturnData=StackData[StackPointer]
        return ReturnData
#Part di
for i in range(11):
    userinp=int(input("Enter 11 numbers:"))
    Temp=Push(userinp)
    if Temp==False:
        print("Unsuccessfull")
    else:
        print("Successfull")
print(StackData)
#Part eii
Pop()
Pop()
Output()


    



