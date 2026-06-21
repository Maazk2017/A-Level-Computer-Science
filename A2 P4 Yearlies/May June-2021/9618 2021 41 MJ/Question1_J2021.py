#Question1 Part a
class node():
    #PUBLIC data:INTEGER
    #PUBLIC nextNode:INTEGER
    def __init__(self,DataP,NextNodeP):
        self.data=DataP
        self.nextNode=NextNodeP
#Part b
#DECLARE LinkedList:ARRAY[0:9] OF node
linkedList=[node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1)]
startPointer=0
emptyList=5
#Part c
def outputNodes():
    global linkedList
    global startPointer
    currentPointer=startPointer
    while currentPointer!=-1:
        print(str(linkedList[currentPointer].data))
        currentPointer=linkedList[currentPointer].nextNode
#Part d
outputNodes()
#Part e
def addNode(currentPointer):
    global linkedList
    global emptyList
    Data=int(input("Enter the data:"))
    if emptyList<0 or emptyList>9:
        return False
    else:
        freeList=emptyList
        emptyList=linkedList[emptyList].nextNode
        newnode=node(Data,-1)
        linkedList[freeList]=newnode
        previousPointer=0
        while currentPointer!=-1:
            previousPointer=currentPointer
            currentPointer=linkedList[currentPointer].nextNode
        linkedList[previousPointer].nextNode=freeList
        return True
#Part f
outputNodes()
result=addNode(startPointer)
if result=="False":
    print("Not Successful")
else:
    print("Successful")
outputNodes()





    
