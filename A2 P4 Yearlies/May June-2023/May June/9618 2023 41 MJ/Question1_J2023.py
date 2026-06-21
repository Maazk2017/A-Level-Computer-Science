#Part ai
#DECLARE DataArray:ARRAY[0:24]OF INTEGER
DataArray=[]
#Part aii
try:
    File=open("Data.txt","r")
    for x in range(25):
        DataArray.append(int(File.readline().strip()))
except IOError:
    print("File Doesn't Exists")
#Part bi
def PrintArray(IntArray):
    for x in range(len(IntArray)):
        print(IntArray[x],end=" ")
    print()
#Part bii
PrintArray(DataArray)
#Part biii
#Part c
def LinearSearch(NewArray,Value):
    count=0
    for x in range(len(NewArray)):
        if NewArray[x]==Value:
            count=count+1
    return count
#Part di
userinp=int(input("Enter the number b/w 1 & 100 inclusive:"))
if userinp<1 or userinp>100:
    print("Invalid number")
else:
    Temp=LinearSearch(DataArray,userinp)
    print("The number",userinp,"is found",Temp)
#Part dii


