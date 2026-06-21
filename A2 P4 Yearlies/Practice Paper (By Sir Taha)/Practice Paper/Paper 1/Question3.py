#Part a
class node():
    #PUBLIC data:INTEGER
    #PUBLIC nextNode:INTEGER
    def __init__(self,data,nextNode):
        self.data=data
        self.nextNode=nextNode
#Part b
#DECLARE LinkedList:ARRAY[0:9]OF node
LinkedList=[node(1,1), node(5,4), node(6,7), node(7,-1), node(2,2), node(0,6), node(0,8), node(56,3), node(0,9), node(0,-1)]
startPointer=0
emptyList=5
#Part ci
def OutputNodes(array,pointer):
    currentpointer=startPointer
    while currentpointer!=-1:
        print(LinkedList[currentpointer].data)
        currentpointer=LinkedList[currentpointer].nextNode
#Part cii
OutputNodes(LinkedList,startPointer)
#Part di
def DeleteNode(DataToRemove):
    global LinkedList
    global emptyList
    global startPointer

    currentpointer=startPointer
    while currentpointer!=-1 and LinkedList[currentpointer].data!=DataToRemove:
        previouspointer=currentpointer
        currentpointer=LinkedList[currentpointer].nextNode
    if currentpointer==-1:
        return False
    else:
        if currentpointer==startPointer:
            startPointer=LinkedList[currentpointer].nextNode
        else:
            LinkedList[previouspointer].nextNode=LinkedList[currentpointer].nextNode
        LinkedList[currentpointer].data=0
        LinkedList[currentpointer].nextNode=emptyList
        emptyList=currentpointer
        return True
#Part dii
print("Before")
OutputNodes(LinkedList,startPointer)
Temp=DeleteNode(56)
if Temp==False:
    print("It doesnot exists")
else:
    print("Successfully Deleted")
print("After")
OutputNodes(LinkedList,startPointer)
#Part diii

