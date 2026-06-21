#Question 1a
#DECLARE Animals:ARRAY[0:9] OF STRING
global Animals
Animals=[""]*10
#Part b
Animals[0]="horse"
Animals[1]="lion"
Animals[2]="rabbit"
Animals[3]="mouse"
Animals[4]="bird"
Animals[5]="deer"
Animals[6]="whale"
Animals[7]="elephant"
Animals[8]="kangroo"
Animals[9]="tiger"
#Part c
def SortDescending():
    global Animals
    ArrayLength=len(Animals)
    for x in range(0,ArrayLength-1):
        for y in range(0,ArrayLength-x-1):
            if Animals[y][0]<Animals[y+1][0]:
                Temp=Animals[y]
                Animals[y]=Animals[y+1]
                Animals[y+1]=Temp
#Part d
SortDescending()
for x in range(10):
    print(Animals[x])
#Question 2a
#DECLARE DataArray:ARRAY[0:24] OF INTEGER
DataArray=[]
#Part b
try:
    File=open("Data.txt","r")
    for x in range(25):
        Data=int(File.readline().strip())
        DataArray.append(Data)
    File.close()
except IOError:
    print("File Doesn't Exists")
#Part c
def PrintArray(array):
    finalstring=""
    for x in range(len(array)):
        finalstring=finalstring+str(array[x])+" "
    print(finalstring)
PrintArray(DataArray)
#Part d
PrintArray(DataArray)
#Part e
#Part f
def LinearSearch(Array,Value):
    count=0
    for x in range(len(Array)):
        if Array[x]==Value:
            count=count+1
    return count
#Part g
Flag=False
while Flag==False:
    num=int(input("Enter the number:"))
    if num>= 0 and num<=100:
        Flag=True
temp=LinearSearch(DataArray,num)
print("The number",num,"is found",temp,"times")





