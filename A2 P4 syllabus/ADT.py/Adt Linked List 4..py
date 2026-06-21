
class node():
    #PUBLIC Data:INTEGER
    #PUBLIC nextNode:INTEGER
    def __init__(self,DataP,nextNodeP):
        self.Data=DataP
        self.nextNode=nextNodeP
#DECLARE LinkedList :ARRAY[0:9] OF node
LinkedList=[node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(56,3),node(0,9),node(0,1)]
startPointer=0 #INTEGER
emptyList=5 #INTEGER
def addNode(currentpointer):
    global LinkedList
    global emptyList
    data=int(input("Enter The That You Want To Add:"))
    #Step1 :Check if you have space or not
    if emptyList<0 or emptyList>9:
        return False
    else:
        #Step2 :Make temporary variable for emptly list
        freelist=emptyList
        #Step3:Increment your emptyist
        emptyList=LinkedList[emptyList].nextNode
        #Step4: Make your node by using freelist
        LinkedList[freelist]=node(data,-1)
        #Step5:Find the index value of last node
        previouspointer=0
        while currentpointer!=-1:
            previouspointer=currentpointer
            currentpointer=LinkedList[currentpointer].nextNode
            #Step6:Now you have the index value of last node in previouspointer
            #Just link them
        LinkedList[previouspointer].nextNode=freelist
        return True
addNode(startPointer)
print("Empty List:",emptyList)
print(LinkedList[5].Data)
print(LinkedList[5].nextNode)
print(LinkedList[3].Data)
print(LinkedList[3].nextNode)
#Deleltion in Linked List
def deleteNode():
    global LinkedList
    global startPointer
    global emptyList
    currentpointer=startPointer
    data=int(input("Enter The Data You Are Trying To Remove"))
    #Step1:find the index of the value which you are trying to remove
    previouspointer=0
    while currentpointer!=-1 and LinkedList[currentpointer].Data!=data:
        previouspointer=currentpointer
        currentpointer=LinkedList[currentpointer].nextNode
    #Step2:When you are outside the loop you will have three options
    # 1) the item that you want to remove is not in the linked list
    # 2) the value you want to remove is the first node so update start pointer
    # 3) the value is in between or the last node 
    if currentpointer==-1:
        return False #means list does not contains that value 
    else:
        #update the pointers accordingly
        #Inrement the start pointer
        if currentpointer==startPointer:
            startPointer=LinkedList[startPointer].nextNode #means the value is the first node
        else:
            LinkedList[previouspointer].nextNode=LinkedList[currentpointer].nextNode
        #Step3:addd the removed node in the empty list
        LinkedList[currentpointer].Data=0
        LinkedList[currentpointer].nextNode=emptyList
        emptyList=currentpointer
        return True
#
def OutputNodes():
    global LinkedList
    global startPointer
    currentpointer=startPointer
    while currentpointer!=-1:
        print(int(LinkedList[currentpointer].Data))
        currentpointer=LinkedList[currentpointer].nextNode
#OutputNodes()
#
def FindItem(currentpointer,SearchValue):
    global LinkedList
    while currentpointer!=-1 and LinkedList[currentpointer].Data!=SearchValue:
        currentpointer=LinkedList[currentpointer].nextNode
    return currentpointer
OutputNodes()
Found=FindItem(startPointer,56)
if Found==-1:
    print("The data you are trying to find is not there")
else:
    print("The value is at position:",Found)
