#Part a
#DECLARE NumData:ARRAY[0:9]OF INTEGER
global NumData
NumData=[10,4,23,45,12,8,21,11,3,1]
#Part bi
def BubbleSort(Array):
    global NumData
    Flag=False
    Boundary=9
    while Flag==False:
        Flag=True
        for y in range(Boundary):
            if NumData[y]>NumData[y+1]:
                Temp=NumData[y]
                NumData[y+1]=NumData[y]
                NumData[y+1]=Temp
        Boundary=Boundary-1
#Part bii
BubbleSort(NumData)
print(NumData)
#Part c
def BinarySearch(number):
    #DECLARE upperbound, lowerbound, midpoint : INTEGER
    #DECALRE valuefound, notinlist : BOOLEAN
    global NumData
    upperbound = 9
    lowerbound = 0
    valuefound = False
    notinlist = False

    while valuefound == False and notinlist == False:
        midpoint = int((upperbound + lowerbound)/2)

        if NumData[midpoint] == number:
            valuefound = True
            return True
        elif NumData[midpoint] < number:
            lowerbound = midpoint + 1
        else:
            upperbound = midpoint - 1

        if lowerbound > upperbound:
            notinlist = True
            return False
        
    
#Part cii
BubbleSort(NumData)
userinp=int(input("Enter a Number:"))
Temp=BinarySearch(userinp)
if Temp==False:
    print("Not Found")
else:
    print("Found")
#Part ciii





