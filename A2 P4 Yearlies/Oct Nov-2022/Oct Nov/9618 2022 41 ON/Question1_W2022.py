#Part a
#DECLARE DataArray:ARRAY[0:99]OF INTEGER
DataArray=[]*100
#Part b
def ReadFile():
    try:
        File=open("IntegerData.txt","r")
        for x in range(100):
            line=int(File.readline().strip())
            DataArray.append(line)
        File.close()
    except IOError:
        print("File Doesn't Exists")
#Part c
def FindValues():
    Number=int(input("Enter the number you want to be found b/w 1 & 100 inclusive:"))
    count=0
    if Number<1 or Number>100:
        print("Invalid")
    else:
        for x in range(len(DataArray)):
            if DataArray[x]==Number:
                count=count+1
        return count
#Part di
ReadFile()
Times=FindValues()
print("The number of times your number repeated is",Times)
#Part dii
def BubbleSort():
    global DataArray
    Boundary=99
    Flag=False
    while Flag==False:
        Flag=True
    for x in range(Boundary):
        if DataArray[x]>DataArray[x+1]:
            Temp=DataArray[x]
            DataArray[x]=DataArray[x+1]
            DataArray[x+1]=Temp
            Flag=False
    Boundary=Boundary-1
BubbleSort()
print(DataArray)


        

