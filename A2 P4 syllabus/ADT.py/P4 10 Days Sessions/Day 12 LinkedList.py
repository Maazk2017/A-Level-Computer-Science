#Part a
#DECLARE LinkedList:ARRAY[0:19,0:1]
global LinkedList
global FirstEmpty #EmpytList
global FirstNode  #StartPointer

FirstEmpty=0 
FirstNode=-1 
LinkedList=[]

for i in range(20):
    LinkedList.append([-1,i+1])
LinkedList[19][1]=-1

for rows in range(20):
    print(LinkedList[rows])
#Part b
def InsertData():
    global LinkedList
    global FirstEmpty
    global FirstNode

    for x in range(5):
        if FirstEmpty!=-1:
            Data=int(input("Enter The Data:"))
            #Incrementation of EmptyList(FirstEmpty)
            FreeList=FirstEmpty
            FirstEmpty=LinkedList[FirstEmpty][1]
            #Make a node
            LinkedList[FreeList][0]=Data
            LinkedList[FreeList][1]=FirstNode
            #Change your startpointer(FirstNode)
            #it will point towards the new added node
            #as each data item is inserted at the front
            FirstNode=FreeList
#Part c
def OutputLinkedlist():
    global LinkedList
    global FirstNode

    CurrentPointer=FirstNode
    while CurrentPointer!=-1:
        print(LinkedList[CurrentPointer][0])
        CurrentPointer=LinkedList[CurrentPointer][1]

#Part d
def RemoveData(DataToRemove):
    global LinkedList
    global FirstEmpty
    global FirstNode
    #Finding the node to be removed
    CurrentPointer=FirstNode
    while CurrentPointer!=-1 and LinkedList[CurrentPointer][0]!=DataToRemove:
        PreviousPointer=CurrentPointer
        CurrentPointer=LinkedList[CurrentPointer][1]
    #You have 2 cases 
    #1)The data to be removed is the firstnode
    if CurrentPointer==FirstNode:
        #Incremet the startpointer as the node has been removed
        FirstNode=LinkedList[FirstNode][1]
    else:
        #Data to remove is in between
        LinkedList[FirstNode][1]=LinkedList[CurrentPointer][1]
    #Adjusting removed node in emptylist
    LinkedList[CurrentPointer][0]=-1
    LinkedList[CurrentPointer][1]=FirstEmpty
    FirstEmpty=CurrentPointer
#Part e
InsertData()
OutputLinkedlist()
RemoveData(5)
print("After")
OutputLinkedlist()