#Part a
class Character():
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
#DECLARE Character:ARRAY[0:9]OF Character
Characters=[]
try:
    File=open("Characters.txt","r")
    for x in range(10):
        NameLine=File.readline().strip()
        XLine=int(File.readline().strip())
        YLine=int(File.readline().strip())
        CharacterObject=Character(NameLine,XLine,YLine)
        Characters.append(CharacterObject)
    File.close()
except IOError:
    print("File Doesn't Exists")
#Part e
Flag=False
while Flag==False:
    username=input("Enter Valid Name:")
    for x in range(10):
        if Characters[x].GetName().lower()==username.lower():
            Store=x
            Flag=True

#Part f
Valid=False
while Valid==False:
    userdir=input("Enter the direction you want to move:")
    if userdir.upper()=="A":
        Characters[Store].ChangePosition(-1,0)
        Valid=True
    elif userdir.upper()=="W":
        Characters[Store].ChangePosition(0,1)
        Valid=True
    elif userdir.upper()=="S":
        Characters[Store].ChangePosition(-1,0)
        Valid=True
    elif userdir.upper()=="D":
        Characters[Store].ChangePosition(1,0)
        Valid=True
    else:
        print("Invalid")
#Part gi 
print(username,"has change XCoordinate to X=",Characters[Store].GetX(),"and YCoordinate to Y=",Characters[Store].GetY())


        

