#Part a
#DECLARE ArrayNodes :2DARRAY [0,2:0,19]OF INTEGER
ArrayNodes=[[-1,-1,-1]for i in range(20)]
RootPointer=-1
FreeNode=0
#Part b
def AddNode():
    global ArrayNodes
    global RootPointer
    global FreeNode
    NodeData=int(input("Enter the NodeData:"))
    if FreeNode<=19:
        ArrayNodes[FreeNode][0]=-1
        ArrayNodes[FreeNode][1]=NodeData
        ArrayNodes[FreeNode][2]=-1
        if RootPointer==-1:
            RootPointer=0
        else:
            CurrentPointer=RootPointer
            Placed=False
            while Placed==False:
                if NodeData<ArrayNodes[CurrentPointer][1]:
                    if ArrayNodes[CurrentPointer][0]==-1:
                        ArrayNodes[CurrentPointer][0]=FreeNode
                        Placed=True
                    else:
                        CurrentPointer=ArrayNodes[CurrentPointer][0]
                else:
                    if ArrayNodes[CurrentPointer][2]==-1:
                        ArrayNodes[CurrentPointer][2]=FreeNode
                        Placed=True
                    else:
                        CurrentPointer=ArrayNodes[CurrentPointer][2]
        FreeNode=FreeNode+1
    else:
        print("Binary Tree is Full")
#Part c
def PrintALL():
    for i in range(20):
        print(ArrayNodes[i][0]," ",ArrayNodes[i][1]," ",ArrayNodes[i][2])
#Part d
for x in range(10):
    AddNode()
PrintALL()
#Part e
def InOrder(Root):
    global ArrayNodes
    global RootPointer
    
    if ArrayNodes[Root][0]!=-1:
        InOrder(ArrayNodes[Root][0])
    print(ArrayNodes[Root][1])
    if ArrayNodes[Root][2]!=-1:
        InOrder(ArrayNodes[Root][2])
InOrder(RootPointer)





        


