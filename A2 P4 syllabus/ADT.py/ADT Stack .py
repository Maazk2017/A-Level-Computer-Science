
       
GujjarTayyara=[""]*5
ChandBhai=0
def Push(Passanger):
    global GujjarTayyara
    global ChandBhai
    if ChandBhai>4:
        print("Tayyara Full Hai")
    else:
        GujjarTayyara[ChandBhai]=Passanger
        ChandBhai=ChandBhai+1
def Pop():
    global GujjarTayyara
    global ChandBhai
    if ChandBhai==0:
        print("Tayyara Khali Hai")
    else:
        ChandBhai=ChandBhai-1
        print (GujjarTayyara[ChandBhai])
Push("Taha")
Push("Bano")
Push("Pappo")
Push("Wasim")
Push("Zeemal")
Pop()
Push("Masroor")
Pop()
Pop()
Pop()
Pop()
Pop()
Pop()

print(GujjarTayyara)
print("ChandBahi seat number",ChandBhai,"per hain")

GujjarTayyara=[""]*5
ChandBhai=-1
def Push(Passanger):
    global GujjarTayyara
    global ChandBhai
    if ChandBhai==4:
        print("Tayyara Full Hai")
    else:
        ChandBhai=ChandBhai+1
        GujjarTayyara[ChandBhai]=Passanger
def Pop():
    global GujjarTayyara
    global ChandBhai
    if ChandBhai==-1:
        print("Tayyara Khali Hai")
    else:
        print (GujjarTayyara[ChandBhai])
        ChandBhai=ChandBhai-1

#Pracrice Question
#DECLARE StackData:ARRAY[0:9] OF INTEGER
#DECLARE StackPointer:INTEGER
global StackData
global StackPointer
StackData=[0]*10
StackPointer=0
#Part b
def Elements():
    global StackData
    global StackPointer
    for i in range(10):
        print(StackData[i])
    print(StackPointer)
#Part c
def Push(Data):
    global StackData
    global StackPointer
    if StackPointer>9:
        return False
    else:
        StackData[StackPointer]=Data
        StackPointer=StackPointer+1
        return True
#Part d
for x in range(11):
    userinp=int(input("Enter Numbers"))
    temp=Push(userinp)
    if temp==False:
        print("Not Added")
    else:
        print("Added")
Elements()
#Part e
Push(11)
Push(12)
Push(13)
Push(14)
Push(15)
Push(16)
Push(17)
Push(18)
Push(19)
Push(20)
Push(21)
#Part f
def Pop():
    global StackData
    global StackPointer
    if StackPointer==0:
     return -1
    else:
        StackPointer=StackPointer-1
        temp=StackData[StackPointer]
        return temp






    








            
    




