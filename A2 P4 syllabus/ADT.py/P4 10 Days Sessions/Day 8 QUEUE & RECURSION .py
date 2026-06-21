#DECLARE Queue : ARRAY [0:99] OF INTEGER
global Queue
global HeadPointer
global TailPointer
HeadPointer = -1
TailPointer = 0
Queue = [0] * 100

def Enqueue(Data):
    global Queue
    global TailPointer
    global HeadPointer

    # IF tailpointer is less than the max index
    #then you have space in Queue
    if TailPointer < 100:
        Queue[TailPointer] = Data
        #Increment Tail Pointer so it points
        # to the next free space
        TailPointer = TailPointer + 1

        #Just for the first enqueue
        # you have to initialize h.p
        if HeadPointer == -1:
            HeadPointer = 0
        return True
    else:
        return False

flag = True      
for num in range(1, 21):
    tempflag = Enqueue(num)
    if tempflag == False:
        flag = False
    
if flag == True:
    print("successfully enqueued")
else:
    print("Unsuccessful")
print(Queue)

def RecursiveOutput(Start):
    if Start<0:
        return 0
    else:
        return Queue[Start]+RecursiveOutput(Start -1)
temp=RecursiveOutput(TailPointer)
print(temp)
