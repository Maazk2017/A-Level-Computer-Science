#Part a
class Tree():
    #PRIVATE TreeName:STRING
    #PRIVATE HeightGrowth:INTEGER
    #PRIVATE MaxHeight:INTEGER
    #PRIVATE MaxWidth:INTEGER
    #PRIVATE EverGreen:STRING
    def __init__(self,TreeName,HeightGrowth,MaxHeight,MaxWidth,EverGreen):
        self.__TreeName=TreeName
        self.__HeightGrowth=HeightGrowth
        self.__MaxHeight=MaxHeight
        self.__MaxWidth=MaxWidth
        self.__EverGreen=EverGreen
#Part aii
    def GetTreeName(self):
        return self.__TreeName
    def GetGrowth(self):
        return self.__HeightGrowth
    def GetMaxHeight(self):
        return self.__MaxHeight
    def GetMaxWidth(self):
        return self.__MaxWidth
    def GetEverGreen(self):
        return self.__EverGreen
#Part b
def ReadData():
#DECLARE TreeArray[0:8] OF Tree
    TreeArray=[]
    try:
        File=open("Trees.txt","r")
        for x in range(9):
            TreeData=File.readline().strip().split(",")
            TreeName=TreeData[0]
            Growth=int(TreeData[1])
            MaxHeight=int(TreeData[2])
            MaxWidth=int(TreeData[3])
            EverGreen=TreeData[4]
            TreeObj=Tree(TreeName,Growth,MaxHeight,MaxWidth,EverGreen)
            TreeArray.append(TreeObj)
        File.close()
    except IOError:
        print("File Doesn't Exists")
    return TreeArray
#Part c
def PrintTrees(TreeObject):
    TreeName=TreeObject.GetTreeName()
    Growth=TreeObject.GetGrowth()
    MaxHeight=TreeObject.GetMaxHeight()
    MaxWidth=TreeObject.GetMaxWidth()
    EverGreen=TreeObject.GetEverGreen()
    if EverGreen=="Yes":
        print(TreeName,"has a maximum height",MaxHeight,"a maximum width",MaxWidth,"and grows",Growth,"cm a year.It does not lose it's leaves")
    else:
        print(TreeName,"has a maximum height",MaxHeight,"a maximum width",MaxWidth,"and grows",Growth,"cm a year.It loses it's leaves each year")
#Part di
ReturnArray=ReadData()
PrintTrees(ReturnArray[0])
#ii
#Part e
def ChooseTree(TreeArray):
    Treeheight=int(input("Enter the tree height:"))
    Treewidth=int(input("Enter tree width:"))
    Evergreen=input("Enter yes or no:")
    TreeArrayChoose=[]
    for x in range(len(TreeArray)):
        if TreeArray[x].GetMaxHeight()<=Treeheight and TreeArray[x].GetMaxWidth()<=Treewidth and TreeArray[x].GetEverGreen().lower()<=Evergreen.lower():
            TreeArrayChoose.append(TreeArray[x])
    if len(TreeArrayChoose)==0:
        print("No matching tree")
    else:
        for x in range(len(TreeArrayChoose)):
            PrintTrees(TreeArrayChoose[x])
#Part eii
    Treename=input("Enter the tree name:")
    TreeHeight=int(input("Enter the tree Height:"))
    for x in range(len(TreeArrayChoose)):
        nameTree=TreeArrayChoose[x].GetTreeName()
        maxheightchosentree=TreeArrayChoose[x].GetMaxHeight()
        growtheachyear=TreeArrayChoose[x].GetGrowth()
        if nameTree.lower()==Treename.lower():
            break
    height=Treeheight-maxheightchosentree
    years=int(height/growtheachyear)
    print(years)
ChooseTree(ReturnArray)
     
        















    




    


