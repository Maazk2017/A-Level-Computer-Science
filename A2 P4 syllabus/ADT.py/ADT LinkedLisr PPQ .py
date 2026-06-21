#ADT LINKEDLIST PPQ
#Question 1 a 1,47
class Node:
    #PUBLIC Data:INTEGER
    #PUBLIC NextNode:INTEGER
    def __init__(self,Datap,NextNodep):
        self.Data=Datap
        self.NextNode=NextNodep
#b
#DECLARE LinkedList:ARRAY[0:8] OF Node
LinkedList=[Node(1,1),Node(5,4),Node(6,7),Node(7,-1),Node(2,2),Node(0,6),Node(0,8),Node(56,3),Node(0,9),Node(0,-1)]
StartPointer=0
EmptyList=5
#c
def OutputNodes():
    global LinkedList
    global StartPointer
    CurrentPointer=StartPointer
    while CurrentPointer!=-1:
        print(int(LinkedList[CurrentPointer].Data))
        CurrentPointer=LinkedList[CurrentPointer].NextNode
#d
OutputNodes()
#e
def AddNode():
    global LinkedList
    global StartPointer
    global EmptyList
    DataToAdd=int(input("Enter The Data You Want To Add:"))
    if EmptyList<0 or EmptyList>9:
        return False
    else:
        FreeList=EmptyList
        EmptyList=LinkedList[EmptyList].NextNode
        LinkedList[FreeList]=(DataToAdd,-1)
        PreviousPointer=0
        while CurrentPointer!=-1:
            PreviousPointer=CurrentPointer
            CurrentPointer=LinkedList[CurrentPointer].NextNode
        LinkedList[PreviousPointer].NextNode=FreeList
        return True
#f
OutputNodes()
returnvalue=AddNode()
if returnvalue==False:
    print("Item no added,List Full")
else:
    print("Item Successfully Added")
OutputNodes()