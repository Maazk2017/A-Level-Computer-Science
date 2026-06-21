#Part a
Colours=[""]*45
def ReadData():
    Colours=[]
    try:
        File=open("Data.txt","r")
        for x in range(45):
            Colours.append(File.readline().strip())
        File.close()
    except IOError:
        print("File Does'nt Exists")
    return Colours
#Part ai
def FormatArray(Array):
    Temp=""
    for x in range(len(Array)):
        Temp=Temp+(Array[x])+" "
    return Temp
#Part aii
TheArray=ReadData()
ReturnArray=FormatArray(TheArray)
print(ReturnArray)
#Part c
def CompareStrings(String1,String2):
    Count=0
    Flag=True
    while Flag==True:
        if String1[Count]<String1[Count]:
            Flag=True
            return 1
        elif String1[Count]>String2[Count]:
            Flag=True
            return 2
        else:
            Count=Count+1
#Part di
def Bubble(DataArray):
    Boundary=len(DataArray)-1
    noswap=False
    while noswap==False:
        noswap=True
        for y in range(Boundary):
            Result=CompareStrings(DataArray[y],DataArray[y+1])
            if Result==2:
                Temp=DataArray[y]
                DataArray[y+1]=DataArray[y]
                DataArray[y]=Temp
        Boundary=Boundary-1
    return DataArray   
#Part dii
Sorted=Bubble(Colours)
print("After")
print(FormatArray(Sorted))

#diii


