#Question 2 Part a
#DECLARE arrayData:ARRAY[0:9]OF INTEGER 
arrayData=[10,5,6,7,1,12,13,15,21,8]
#Part bi
def linearSearch(number):
    Flag=False
    for x in range(len(arrayData)):
        if arrayData[x]==number:
            Flag=True
            break
    if Flag==False:
        return False
    else:
        return True
#Part bii
userinp=int(input("Enter a number:"))
temp=linearSearch(userinp)
if temp==True:
    print("Found")
else:
    print("Not Found")
#Part biii

#Part ci
def BubbleSort(theArray):
    for x in range(0,len(theArray)):
        for y in range(0,len(theArray)-x-1):
            if theArray[y]<theArray[y+1]:
                temp=theArray[y]
                theArray[y]=theArray[y+1]
                theArray[y+1]=temp
BubbleSort(arrayData)
print(arrayData)




