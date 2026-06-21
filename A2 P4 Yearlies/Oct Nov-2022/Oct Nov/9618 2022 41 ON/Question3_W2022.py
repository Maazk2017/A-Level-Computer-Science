#Part a
#DECLARE ArrayNodes:ARRAY[0:19,0:2]OF INTEGER
ArrayNodes=[[-1,-1,-1] for i in range(20)]
#Sir taha method 
#ArrayNodes=[]
#for i in range(20):
#   ArrayNodes[-1,-1,-1]
#because it said to intialize each node to -1
#Part b
ArrayNodes=[[1,20,5],[2,15,-1],[-1,3,3],[-1,9,4],[-1,10,-1],[-1,58,-1],[-1,-1,-1]]
Freenode=6
RootPointer=0
#Part c
def SearchValue(Root,ValueToFind):
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
#Part d
def PostOrder(Root):
    global ArrayNodes
    if ArrayNodes[Root][0]!=-1:
        PostOrder(ArrayNodes[Root][0])
    if ArrayNodes[Root][2]!=-1:
        PostOrder(ArrayNodes[Root][2])
    print(ArrayNodes[Root][1])
#Part ei
Temp=SearchValue(RootPointer,15)
if Temp==-1:
    print("Value not in the BinaryTree")
else:
    print("The Index of the Value is",Temp)
PostOrder(RootPointer)
#Part eii

    

    
