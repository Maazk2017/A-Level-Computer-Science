#Part a
#DECLARE Datatored:ARRAY[0:19]OF INTEGER
#DECLARE NumberOfItems:INTEGER
global DataStored
global NumberOfItems
DataStored=[]
#Part b
def Initialise():
    global DataStored
    global NumberOfItems
    Valid=False
    while Valid==False:
        NumberOfItems=int(input("Enter the quantity of numbers:"))
        if NumberOfItems>0 and NumberOfItems<21:
            Valid=True
    for i in range(NumberOfItems): 
        usernum=input("Enter the numbers:") 
        DataStored.append(int(usernum))
#Part ci
NumberOfItems=0
Initialise()
print(DataStored)
#Part cii
#Part di
def BubbleSort():
    global DataStored
    global NumberOfItems
    noswap=False
    Boundary=NumberOfItems-1
    while noswap==False:
        noswap=True
        for y in range(Boundary):
            if DataStored[y]>DataStored[y+1]:
                Temp=DataStored[y]
                DataStored[y]=DataStored[y+1]
                DataStored[y+1]=Temp
                noswap=False
        Boundary=Boundary-1
#Part dii
BubbleSort()
print(DataStored)
#Part ei
def BinarySearch(DataToFind):
    global DataStored
    global NumberItems

    upperbound = NumberItems - 1
    lowerbound = 0
    valuefound = False
    notinthelist = False

    while valuefound == False and notinthelist == False:

        midpoint = int((upperbound + lowerbound) / 2)

        if DataStored[midpoint] == DataToFind:
            valuefound = True
            return midpoint
        elif DataStored[midpoint] < DataToFind:
            lowerbound = midpoint + 1
        else:
            upperbound = midpoint - 1
        
        if lowerbound > upperbound:
            notinthelist = True
            return -1
#Part eii
userinp=int(input("Enter a number:"))
Temp=BinarySearch(userinp)
print(Temp)