class node:
    # PUBLIC Data : INTEGER
    # PUBLIC nextNode : INTEGER
    def __init__(self, DataP, nextNodeP):
        self.Data = DataP
        self.nextNode = nextNodeP

# DECLARE startPointer, emptyList : INTEGER
# DECLARE LinkedList : ARRAY [0:9] OF node
LinkedList = [node(1,1), node(5,4), node(12,7), node(41,-1), node(8,2), node(0,6), node(0,8), node(32,3), node(0,9), node(0,-1) ]

startPointer = 0
emptyList = 5

def outputNode(array, currentpointer):
    while currentpointer != -1:
        print(array[currentpointer].Data)
        currentpointer = array[currentpointer].nextNode


def Addnode(datatoinsert, currentpointer):
    global LinkedList
    global emptyList
    global startPointer

    if emptyList < 0 or emptyList > 9:
        return False
    else:
        freelist = emptyList
        emptyList = LinkedList[emptyList].nextNode

        newNode = node(datatoinsert, -1)

        LinkedList[freelist] = newNode

        while currentpointer != -1 and LinkedList[currentpointer].Data < datatoinsert:
            previouspointer = currentpointer
            currentpointer = LinkedList[currentpointer].nextNode

        if currentpointer == startPointer:
            LinkedList[freelist].nextNode = startPointer
            startPointer = freelist
        else:
            LinkedList[freelist].nextNode = LinkedList[previouspointer].nextNode
            LinkedList[previouspointer].nextNode =freelist

        return True

outputNode(LinkedList, startPointer)
temp = Addnode(67, startPointer)
outputNode(LinkedList, startPointer)

if temp == True:
    print("Value Added")
else:
    print("Not Added")
































