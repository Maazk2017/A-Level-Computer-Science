#Binary Searching
#Q1:Linear Searching
#Part A:Declaration
#Declare arraydata :ARRAY [0:9] OF INTEGER
arraydata=[10,5,6,7,1,12,13,15,21,8]
#Part B
def linearsearching(value):
    for x in range(len(arraydata)):
        if arraydata[x]==value:
            return True
    return False 
#Part B(ii)
temp=int(input("Enter a number:"))
found=linearsearching(temp)
if found==True:
    print("Present")
else:
    print("not there")


#Binary Searching
#CODE
array=[1,5,6,7,8,10,12,13,15,21]
def binarysearch(number):
    #if we dont know the array then 
    # upperbound=len(array)-1
    upperbound=9
    lowerbound=0
    valuefound=False  #to stop the loop
    notinlist=False   #if data is not in array
    while valuefound==False and notinlist==False:
        midpoint=int((lowerbound+upperbound) /2)
        if array[midpoint]==number:
            valuefound=True
            return True
        elif array[midpoint]<number:
            lowerbound=midpoint+1
        else:
            upperbound=midpoint-1
        if lowerbound>upperbound:
            notinlist=True
            return False
temp_1=int(input("Enter a number:"))
Found=binarysearch(temp_1)
if Found==True:
    print("Found")
else:
    print("Not found")



     


