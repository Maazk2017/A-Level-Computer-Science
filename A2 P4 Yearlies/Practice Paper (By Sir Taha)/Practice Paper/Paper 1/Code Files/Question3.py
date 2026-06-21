class node:
    # PUBLIC Data : INTEGER
    # PUBLIC nextNode : INTEGER
    def __init__(self, DataP, nextNodeP):
        self.Data = DataP
        self.nextNode = nextNodeP

# DECLARE LinkedList : ARRAY [0:9] OF node
LinkedList = [node(1,1), node(5,4), node(6,7), node(7,-1), node(2,2), node(0,6), node(0,8), node(56,3), node(0,9), node(0,-1) ]

startPointer = 0
emptyList = 5



def deleteNode(datatoremove):
    global LinkedList
    global startPointer
    global emptyList

    currentPointer = startPointer

    previouspointer = 0
    while currentPointer != -1 and LinkedList[currentPointer].Data != datatoremove:
        previouspointer = currentPointer
        currentPointer = LinkedList[currentPointer].nextNode

    if currentPointer == -1:
        return False
    else:
        if currentPointer == startPointer:
            startPointer = LinkedList[currentPointer].nextNode
        else:
            LinkedList[previouspointer].nextNode = LinkedList[currentPointer].nextNode

        LinkedList[currentPointer].Data = 0
        LinkedList[currentPointer].nextNode = emptyList
        emptyList = currentPointer
        return True

def outputNode(array, currentpointer):
    while currentpointer != -1:
        print(array[currentpointer].Data)
        currentpointer = array[currentpointer].nextNode




outputNode(LinkedList, startPointer)
temp = deleteNode(56)
outputNode(LinkedList, startPointer)

if temp == False:
    print("It does not exist")
else:
    print("Successfully Deleted")

