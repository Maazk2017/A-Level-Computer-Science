def IterativeCalculate(Number):
    ToFind=Number
    Total=0
    while Number!=0:
        if ToFind%Number==0:
            Total=Total+Number
        Number=Number-1
    return Total


temp1=IterativeCalculate(10)
print(temp1)

def RecursiveValue(Number,ToFind):
    if Number==0:
        return 0
    elif ToFind%Number==0:
        return Number+RecursiveValue(Number-1,ToFind)
    else:
        return RecursiveValue(Number-1,ToFind)


temp2=RecursiveValue(50,50)
print(temp2)
         