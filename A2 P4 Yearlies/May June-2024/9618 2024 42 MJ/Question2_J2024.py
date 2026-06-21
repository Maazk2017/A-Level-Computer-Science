#Part ai
class Node():
    #PRIVATE LeftPointer:INTEGER
    #PRIVATE Data:INTEGER
    #PRIVATE RightPointer:INTEGER
    def __init__(self,Data):
        self.__Data=Data
        self.__LeftPointer=-1
        self.__RightPointer=-1
#Part aii
    def GetLeft(self):
        return self.__LeftPointer
    def GetRight(self):
        return self.__RightPointer
    def GetData(self):
        return self.__Data
#Part aiii
    def SetLeft(self,NewLeftPointer):
        self.__LeftPointer=NewLeftPointer
    def SetRight(self,NewRightPointer):
        self.__RightPointer=NewRightPointer
    def SetData(self,NewData):
        self.__Data=NewData
#Part b
class TreeClass():
    #PRIVATE Tree:ARRAY[0:19]OF Node
    #PRIVATE FirstNode:INTEGER
    #PRIVATE NumberNodes:INTEGER
    def __init__(self):
        self.__FirstNode=-1
        self.__NumberNodes=0
        self.__Tree=[]
        for x in range(20):
            self.__Tree.append(Node(-1))
#Part bii
    def InsertNode(self,NewNode):
        if self.__NumberNodes<=19:
            self.__Tree[self.__NumberNodes]=NewNode
            if self.__FirstNode==-1:
                self.__FirstNode=0
            else:
                CurrentPointer=self.__FirstNode
                Placed=False
                while Placed==False:
                    if NewNode.GetData()<self.__Tree[CurrentPointer].GetData():
                       if self.__Tree[CurrentPointer].GetLeft()==-1:
                         self.__Tree[CurrentPointer].SetLeft()=self.__NumberNodes
                         Placed=True
                    else:
                        CurrentPointer=self.__Tree[CurrentPointer].GetLeft()
                else:
                    if self.__Tree[CurrentPointer].GetRight()==-1:
                        self.__Tree[CurrentPointer].SetRight()=self.__NumberNodes
                        Placed=True
                    else:
                        CurrentPointer=self.__Tree[CurrentPointer].GetRight()
        else:
            self.__NumberNodes=self.__NumberNodes+1
#Part biii
    def OutputTree(self):
        if self.__NumberNodes==0:
            print("No Nodes")
        else:
            for x in range(self.__NumberNodes):
                LeftP=self.__Tree[x].GetLeft()
                RightP=self.__Tree[x].GetRight()
                DataP=self.__Tree[x].GetData()
                print("LeftPointer",LeftP)
                print("RightPointer",RightP)
                print("Data",DataP)
#Part ci
TheTree=TreeClass()
#Part cii
TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(7))
TheTree.InsertNode(Node(15))
Temp=TheTree.OutputTree()
print(Temp)



                    