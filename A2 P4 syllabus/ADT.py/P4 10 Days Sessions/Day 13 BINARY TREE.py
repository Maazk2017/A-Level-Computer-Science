class Node():
    #PRIVATE LeftPointer:INTEGER 
    #PRIVATE Data:INTEGER
    #PRIVATE RightPointer:INTEGER
    def __init__(self,DataP):
        self.__LeftPointer=-1
        self.__Data=DataP
        self.__RightPointer=-1
    def GetLeft(self):
        return self.__LeftPointer
    def GetRight(self):
        return self.__RightPointer
    def GetData(self):
        return self.__Data
    def SetLeft(self,LeftP):
        self.__LeftPointer=LeftP
    def SetRight(self,RightP):
        self.__RightPointer=RightP
    def SetData(self,DataP):
        self.__Data=DataP
class TreeClass(Node):
    #PRIVATE Tree:ARRAY [0:19] OF Node
    #PRVATE FirstNode:INTEGER  #Basically RootPointer
    #PRIVATE NumberOfNode:INTEGER #Basically FreeNode
    def __init__(self,DataP):
        super().__init__(DataP)
        self.__FirstNode=-1 #Basically RootPointer
        self.__NumberNodes=0 #Basically FreeNode
        self.__Tree=[]
        for x in range(20):
            self.__Tree.append(Node(-1))
    def InsertNode(self,NewNode):
        if self.__NumberNodes<=19:
            self.__Tree[self.__NumberNodes]=NewNode
            
            if self.__FirstNode==-1:
                self.__FirstNode=0
            else:
                Placed=False
                CurrentPointer=self.__FirstNode
                while Placed==False:
                    if NewNode.GetData()<self.__Tree[CurrentPointer].GetData():
                        if self.__Tree[CurrentPointer].GetLeft()==-1:
                            self.__Tree[CurrentPointer].SetLeft(self.__NumberNodes)
                            Placed=True
                        else:
                            CurrentPointer=self.__Tree[CurrentPointer].GetLeft()
                    else:
                        if self.__Tree[CurrentPointer].GetRight()==-1:
                            self._Tree[CurrentPointer].SetRight(self.__NumberNodes)
                            Placed=True
                        else:
                            CurrentPointer=self.__Tree[CurrentPointer].GetRight()
            self.__NumberNodes=self.__NumberNodes+1
        else:
            print("Binary Tree is Full")
    def OutputNodes(self):
        if self.__NumberNodes==0:
            print("No Nodes")
        else:
            for index in range(self.__NumberNodes):
                LeftPointer=self.__Tree[index].GetLeft()
                RigthPointer=self.__Tree[index].GetRight()
                Data=self.__Tree[index].GetData()
                print("LeftPointer",LeftPointer)
                print("Right Pointer",RigthPointer)
                print("Data",Data)
TheTree=TreeClass(0)
TheTree.InsertNode(10)
TheTree.InsertNode(11)
TheTree.InsertNode(5)
TheTree.InsertNode(1)
TheTree.InsertNode(20)
TheTree.InsertNode(7)
TheTree.InsertNode(15)
TheTree.OutputNodes()
               


            

        


