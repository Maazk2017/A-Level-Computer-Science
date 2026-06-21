class Character():
#Part a
    #PRIVATE Name:STRING
    #PRIVATE XCoordinate:INTEGER
    #PRIVATE YCoordinate:INTEGER
    def __init__(self,Name,XCoordinate,YCoordinate):
        self.__Name=Name
        self.__XCoordinate=XCoordinate
        self.__YCoordinate=YCoordinate
#Part b
    def GetName(self):
        return self.__Name
    def GetX(self):
        return self.__XCoordinate
    def GetY(self):
        return self.__YCoordinate
#Part c
    def ChangePosition(self,XChange,YChange):
        self.__XCoordinate=self.__XCoordinate+XChange
        self.__YCoordinate=self.__YCoordinate+YChange
#Part d
#DECLARE CharacterArray:ARRAY[0:9] OF STRING
Characters=[]
try:
    File=open("Characters.txt","r")
    for x in range(10):
        Name=File.readline().strip()
        XPos=int(File.readline().strip())
        YPos=int(File.readline().strip())
        CharacterObject=Character(Name,XPos,YPos)
        Characters.append(CharacterObject)
except:
    print("File Doesn't Exists or Incorrect File Name")
#Part e
Flag=True
while Flag==True:
    username=input("Enter the name:")
    for x in range(10):
        namefromobject=Characters[x].GetName()
        if username.lower()==namefromobject.lower():
            Position=x
            Flag=False
#Part f
Valid=False
while Valid==False:
    userinp=input("Enter Valid Character")
    if userinp.upper()=="A":
        Characters[Position].ChangePosition(-1,0)
        Valid=True
    elif userinp.upper()=="W":
        Characters[Position].ChangePosition(0,1)
        Valid=True
    elif userinp.upper()=="S":
        Characters[Position].ChangePosition(0,-1)
        Valid=True
    elif userinp.upper()=="D":
        Characters[Position].ChangePosition(1,0)
        Valid=True
#Part g
print(username,"Has changed coordinates to x=",Characters[Position].GetX(),"and Y=",Characters[Position].GetY())
#Part h



   
