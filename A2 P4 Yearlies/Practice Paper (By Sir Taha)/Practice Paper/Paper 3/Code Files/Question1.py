#DECLARE StackPointer : INTEGER
#DECLARE StackData : ARRAY[0:9]
StackPointer = 0
StackData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def PrintArray():
    global StackData
    global StackPointer
    print("The Stack Pointer is", StackPointer)
    for x in range(10):
        print(StackData[x])

def Push(value):
    global StackData
    global StackPointer
    if StackPointer > 9:
        return False
    else:
        StackData[StackPointer] = value
        StackPointer = StackPointer + 1
        return True

for x in range(0,11):
    value = int(input("Enter the number: "))
    if Push(value) == True:
        print("Successfully Added")
    else:
        print("The Stack is Full")

PrintArray()

def Pop():
    global StackData
    global StackPointer
    if StackPointer == 0:
        return -1
    else:
        StackPointer = StackPointer - 1
        temp = StackData[StackPointer]
        StackData[StackPointer] = 0
        return temp

firstpop = Pop()
Secondpop = Pop()

PrintArray()
