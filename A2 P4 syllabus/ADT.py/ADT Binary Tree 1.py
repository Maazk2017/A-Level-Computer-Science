#LinkedList with 2D Arrays
LinkedList=[(1,1),(5,4),(6,2),(0,1)]#row & column
Data=print("Data",LinkedList[1][0])#first one is index 
Pointer=print("Pointer",LinkedList[1][1])#first one is index 
#Binary Tree Addition
#CREATING ARRAY FRO BINARY TREE
ArrayNodes=[[0]*3 for x in range(20)]#3 cols and 20 rows
RootPointer=-1
FreeNode=0
def AddNode():
    global ArrayNodes
    global RootPointer
    global FreeNode
    #Step1:Take input for the value you need to add
    NodeData=int(input("Enter the data:"))
    #Step2:Check if there is space or not
    if FreeNode<=19:
        #Step3:Create a node by using FreeNode
        ArrayNodes[FreeNode][0]=-1
        ArrayNodes[FreeNode][1]=NodeData
        ArrayNodes[FreeNode][2]=-1
        #Step5:Adjusting Pointers
        #we have 2 cases in adjusting pointers
        #Case1)the value is the first in the binary tree
        #Case2)comparison and then store
        if RootPointer==-1:
            RootPointer=0
        else: #Case2) comparison
            Placed=False
            CurrentPointer=RootPointer
            while Placed==False:
                #Cmoparison with the Root Value
                if NodeData<ArrayNodes[CurrentPointer][1]:
                    #if it is smaller value the left
                    #first check if it is empty and store
                    #not empty then increment currentpointer
                    if ArrayNodes[CurrentPointer][0]==-1:
                     ArrayNodes[CurrentPointer][0]=FreeNode
                     Placed=True
                    else:
                        #increment current pointer
                        CurrentPointer=ArrayNodes[CurrentPointer][0]
                else:
                    #if it is greater value than the root
                    if ArrayNodes[CurrentPointer][2]==-1:
                        ArrayNodes[CurrentPointer][2]=FreeNode
                        Placed=True
                    else:
                        #Incremnet on the right side
                        CurrentPointer=ArrayNodes[CurrentPointer][2]
        FreeNode=FreeNode+1
    else:
        print("Binary Tree is Full")

#How th search in a binary tree
def FindNode(SearchItem):
    global RootPointer
    currentpointer=RootPointer
    #Start with root if greater increment right if smaller than root increment left
    while currentpointer!=-1 and ArrayNodes[currentpointer][1]!=SearchItem:
        if SearchItem<ArrayNodes[currentpointer][1]:
            currentpointer=ArrayNodes[currentpointer][0]
        else:
            currentpointer=ArrayNodes[currentpointer][2]
    return currentpointer 
print(RootPointer)
print(FreeNode)
AddNode()
AddNode()
AddNode()
AddNode()
AddNode()
for x in range(4):
    AddNode()
for x in range(20):
    print(ArrayNodes[x])
print(RootPointer)
print(FreeNode)
print(FindNode(12))
#TRAVERSAL 
#Inorder
BinaryTree=[(1,20,5),(2,15,-1),(-1,3,3),(-1,9,4),(-1,10,-1),(-1,58,-1),(-1,-1,-1)]
def InOrder(Root):
    global BinaryTree
    #Left Root Right
    if BinaryTree[Root][0]!=-1:
        InOrder(BinaryTree[Root][0]) #InOrder(BinaryTree[Root].LeftPointer)
    print(BinaryTree[Root][1])  #print(BinaryTree[Root].Data)
    if BinaryTree[Root][2]!=-1:
        InOrder(BinaryTree[Root][2])
InOrder(RootPointer)
#PreOrder
def PreOrder(Root):
    global BinaryTree
    #Root Left Right
    print(BinaryTree[Root][1])
    if BinaryTree[Root][0]!=-1:
        PreOrder(BinaryTree[Root][0])
    if BinaryTree[Root][2]!=-1:
        PreOrder(BinaryTree[Root][2])
#PostOrder
def PostOrder(Root):
    global BinaryTree
    #Left Right Root
    if BinaryTree[Root][0]!=-1:
        PostOrder(BinaryTree[Root][0])
    if BinaryTree[Root][2]!=-1:
        PostOrder(BinaryTree[Root][2])
    print(BinaryTree[Root][1])

