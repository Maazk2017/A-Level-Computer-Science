#Part ai
def IterativeCalculate(Number):
    ToFind=Number
    Total=0
    while Number!=0:
        if ToFind%Number==0:
            Total=Total+Number
        Number=Number-1
    return Total
#Part aii
Temp=IterativeCalculate(10)
print("Iterative",Temp)
#Part aiii
#Part bi
def Recursiveoutput(Number,ToFind):
    if Number==0:
        return 0
    else:
        if ToFind%Number==0:
           return Number+Recursiveoutput(Number-1,ToFind)
        else:
            return Recursiveoutput(Number-1,ToFind)
#Part bii
Temp=Recursiveoutput(50,50)
print("Recursive",Temp)
#Part biii
