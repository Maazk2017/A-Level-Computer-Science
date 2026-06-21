#Part a
#DECLARE NameData:ARRAY[0:6]OF STRING
global NameData
NameData=["Farjad","Khadija","Ali","Mazin","Taha","Fakhir","Zainab"]
#Part bi
def LinearSearch(Value):
    Flag=False
    global NameData
    for x in range(len(NameData)):
        if NameData[x]==Value:
            return True
    return False
#Part bii
userinp=input("Enter the data to be searched:")
Temp=LinearSearch(userinp)
if Temp==False:
    print("Not Found")
else:
    print("Found")
#Part biii
#Part c
def InsertionSort():
    arraysize=len(NameData)
    for pointer in range(1,arraysize):
        valuetoinsert=NameData[pointer]
        holeposition=pointer
        while holeposition>0 and NameData[holeposition-1]>valuetoinsert:
            NameData[holeposition]=NameData[holeposition-1]
            holeposition=holeposition-1
        NameData[holeposition]=valuetoinsert
#Part d
InsertionSort()
print(NameData)
    




   
