#ADT BINARY TREE PPQ
#Question 2a 4
#Binary Tree
#DECLARE ArrayNodes:2D ARRAY [0:2,0:19] OF INTEGER
ArrayNodes=[(0)*3 for i in range(20)]
RootPointer=-1
FreeNode=0
#b
def AddNode():
    global ArrayNodes
    global RootPointer
    global FreeNode
    NodeData=int(input("Enter the Data:"))
    if FreeNode<=19:
        ArrayNodes[FreeNode][0]=-1
        ArrayNodes[FreeNode][1]=NodeData
        ArrayNodes[FreeNode][2]=-1
        if RootPointer==-1:
            RootPointer=0
        else:
            Placed=False
            CurrentPointer=RootPointer
            while Placed==True:
                if NodeData<ArrayNodes[CurrentPointer][1]:
                    if ArrayNodes[CurrentPointer][0]==-1:
                        ArrayNodes[CurrentPointer][0]=FreeNode
                        Placed=True
                    else:
                        CurrentPointer=ArrayNodes[CurrentPointer][0]
                else:
                    if ArrayNodes[CurrentPointer][2]==-1:
                        ArrayNodes[CurrentPointer][2]==FreeNode
                        Placed=True
                    else:
                        CurrentPointer=ArrayNodes[CurrentPointer][2]
        FreeNode=FreeNode+1
    else:
        print("Binary Tree is Full")     
#c
def PrintAll(ArrayNodes):
    for x in range(20):
        print(str(ArrayNodes[x][0]," ",str(ArrayNodes[x][1])," ",str(ArrayNodes[x][2])))
#d
for x in range(10):
    AddNode()
PrintAll()
#e
def InOrder(ArrayNode,RootNode):
    #Left Root Right
    if ArrayNode[RootNode][0]!=-1:
        InOrder(ArrayNode[RootNode][0])
    print(ArrayNode[RootNode][1])
    if ArrayNode[RootNode][2]!=-1:
        InOrder(ArrayNode[RootNode][2])
#Question 5a 13 62
#Binary Tree
#DECALRE ArrayNodes:ARRAY [0:19,0:2] OF INTEGER
ArrayNodes=[]
for x in range(0,20):
    ArrayNodes.append([-1,-1,-1])
#b
ArrayNodes=[(1,20,5),(2,15,-1),(-1,3,3),(-1,9,4),(-1,10,-1),(-1,58,-1),(-1,-1,-1)]
FreeNode=6
RootPointer=0
#c
def SearchValue(Root,ValueToFind):
    global RootPointer
    global FreeNode
    global ArrayNodes
    if Root==-1:
        return -1
    elif ArrayNodes[Root][1]==ValueToFind:
        return Root
    elif ArrayNodes[Root][1]==-1:
        return -1
    if ArrayNodes[Root][1]>ValueToFind:
        return SearchValue(ArrayNodes[Root][0],ValueToFind)
    if ArrayNodes[Root][1]<ValueToFind:
        return SearchValue(ArrayNodes[Root][2],ValueToFind)
#d
def PostOrder(RootNode):
    if ArrayNodes[RootNode][0]!=-1:
        PostOrder(ArrayNodes[RootNode][0])
    if ArrayNodes[RootNode][2]!=-1:
        PostOrder(ArrayNodes[RootNode][2])
    print(str(ArrayNodes[RootNode][1]))
#e
ReturnValue=SearchValue(RootPointer,15)
if ReturnValue==-1:
    print("NotFound")
else:
    print("Found At" + str(ReturnValue))
PostOrder(ArrayNodes[ReturnValue])
#Question 12a
#BinaryTree
#Will do it later in 10days session





