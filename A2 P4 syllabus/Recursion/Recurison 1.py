#Recursion
def recursion(x):
    y=x*2
    print(y)
    if y<10000:
        recursion(y)
recursion(4)
#Stack concept
def recursion(x):
    y=x*2
    if y<10000:
        recursion(y)
        print(y)
recursion(4)
#Winding
#general case in which the fuction calls are getting pushed in the stack no calculation is done in this place
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
temp=factorial(5)
print(temp)
#Unwinding
#when the base case is reached all the data stored in stack gets popped out from top of the stack

#Past Paper Question
def Unknown(X,Y):
    if X<Y:
        print(X+Y)
        return(Unknown(X+1,Y)*2)
    elif X==Y:
        return 1
    else:
        print(X+Y)
        return(Unknown(X-1,Y)//2)
temp=Unknown(10,14)
print(temp)
#Convert it into iterative form
def IterativeUnknown(X,Y):
    total=1
    while X!=Y:
        if X<Y:
         print(X+Y)
         X=X+1
         total=total*2
        else:
            print(X+Y)
            X=X-1
            total=total//2
    return total
temp=IterativeUnknown(10,14)
print("IterativeUnknown:",temp)


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

#STEPS TO WRITE ITERATIVE TO RECURSIVE

#Step1:Understand the iterative code by dry run
#Step2:Figure out the base case
#      by seeing the loops condition
#Step3:Figure out the calculation
#Step4:Count=0 return 0 in base case
#      Total=1 return 1 in base case
#Step5:Calculion should be done recursive calls
#      count=count+1
#      return recursivecount(index+1)+1
#
#      Total=Total+num
#      return recursivenum(index+1)+num
