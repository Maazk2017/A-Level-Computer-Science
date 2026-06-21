

#QUEUE
#DECLARE Names :ARRAY[0:9] OF STRING
Names=[""]*10
HeadPointer=-1
TailPointer=0
def Enqueue(Data):
    global Names
    global HeadPointer
    global TailPointer
    if TailPointer<10:
        Names[TailPointer]=Data
        TailPointer=TailPointer+1
        if HeadPointer==-1:
            HeadPointer=0
    else:
        print("Queue Is Full")
def Dequeue():
    global Names
    global HeadPointer
    global TailPointer
    if HeadPointer==-1:
        print("Queue is Empty")
    else:
        item=Names[HeadPointer]
        HeadPointer=HeadPointer+1
        print(item)
    if HeadPointer==TailPointer:
        TailPointer=0
        HeadPointer=-1
Enqueue("Taha")
Enqueue("Ali")
Enqueue("Dania")
Enqueue("Bano")
Enqueue("Aun")
Enqueue("Jamil")
Enqueue("Shabana")
Enqueue("Fazila")
Enqueue("Massoma")
Enqueue("Ramazan")
Dequeue()
Dequeue()
Dequeue()
Enqueue("Haider")
#This is when concept of circular queue is introduced
print(Names)

#Circular Queue
#DECLARE Queue : ARRAY [0:9] OF STRING
global Headpointer
global Tailpointer
global NumberOFItems
Headfpointer=0
Tailpointer=0
NumberOfItems=0
QueueArray=[""]*10
def Enqueue(DataToAdd):
#can't pass parameter as byref in python so have to declare them as global 
    if NumberOfItems>=10:
        return False
    QueueArray[Tailpointer]=DataToAdd
    if Tailpointer>=9:
        Tailpointer=0
    else:
        Tailpointer=Tailpointer+1
    NumberOfItems=NumberOfItems+1
    return True
#DECLARE Kababjees:ARRAY [0:9] OF STRING
Kabajees=[""]*10
HeadPointer=-1
TailPointer=0
def Enqueue(Customer):
    global Kabajees
    global HeadPointer
    global TailPointer
    if TailPointer<10:  #or if TailPointer==9:
        Kabajees[TailPointer]=Customer
        TailPointer=TailPointer+1
        if HeadPointer==-1:
            HeadPointer=0
    else:
        print("Queue is full")
def Dequeue():
    global Kabajees
    global TailPointer
    global HeadPointer
    if HeadPointer==-1:
        print("Queue is empty")
    else:
        item=Kabajees[HeadPointer]
        HeadPointer=HeadPointer+1
        print(item)
    if HeadPointer==TailPointer:
        HeadPointer=-1
        TailPointer=0

Enqueue("Taha")
Enqueue("Bano")
Enqueue("Qasim")
Enqueue("Anas")
Enqueue("Zulekah")
Enqueue("ali")
Enqueue("Aun")
Enqueue("Fakhir")
Enqueue("Asma")
Enqueue("Haimd")
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Enqueue("Maaz")

print(Kabajees)
print("The TailPointer:",TailPointer)
print("The HeadPointer:",HeadPointer)
#Circular Queue
#DECLARE QueueArray:ARRAY[0:9] OF STRING
#DECLARE HeadPointer,TailPointer,NumberOfItems:INTEGER

HeadPointer=0
TailPointer=0
NumberOfItems=0
QueueArray=[""]*10
def Enqueue(DataToAdd):
    global HeadPointer
    global TailPointer
    global QueueArray
    global NumberOfItems
    if NumberOfItems==10: #menas queue is full
        return False
    QueueArray[TailPointer]=DataToAdd
    if TailPointer>=9:
        TailPointer=0
    else:
        TailPointer=TailPointer+1
    NumberOfItems=NumberOfItems+1 #Item added s0 +1 until no of itmes ==10
    return True
def Dequeue():
    global HeadPointer
    global TailPointer
    global QueueArray
    if HeadPointer==0:
        return "FALSE"
    else:
        value=QueueArray[HeadPointer]
        HeadPointer=HeadPointer+1
    if HeadPointer>9:
        HeadPointer=0
    NumberOfItems=NumberOfItems-1
    return value
Enqueue("A")
Enqueue("B")
print(QueueArray)
print("Number Of Items is",NumberOfItems)
print("Head Pointer is:",HeadPointer)
print("Tail Pointer is:",TailPointer)

    













    
        




    


