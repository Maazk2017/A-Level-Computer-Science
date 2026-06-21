#Part a
#DECLARE NumberArray:ARRAY[0:6]OF INTEGER
NumberArray=[100,85,644,22,15,8,1]
#Part bi
def RecursiveInsertion(IntegerArray,NumberElements):
    if NumberElements<=1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray,NumberElements-1)
        LastItem=IntegerArray[NumberElements-1]
        CheckItem=NumberElements-2
    LoopAgain=True
    if CheckItem<0:
        LoopAgain=False
    else:
        if IntegerArray[CheckItem]<=LastItem:
            LoopAgain=False
    while LoopAgain:
        IntegerArray[CheckItem+1]=IntegerArray[CheckItem]
        CheckItem=CheckItem-1
        if CheckItem<0:
            LoopAgain=False
        else:
            if IntegerArray[CheckItem]<=LastItem:
                LoopAgain=False
    IntegerArray[CheckItem+1]=LastItem
    return IntegerArray
#Part bii
Temp=RecursiveInsertion(NumberArray,7)
print("Recursive",Temp)
#Part biii
#Part ci
def IterativeInsertion(IntegerArray,NumberElements):
    while NumberElements>0:
        LastItem=IntegerArray[NumberElements-1]
        CheckItem=NumberElements-2
        LoopAgain=True
        if CheckItem<0:
            LoopAgain=False
        elif IntegerArray[CheckItem]<=LastItem:
            LoopAgain=False
        while (LoopAgain):
            IntegerArray[CheckItem+1]=IntegerArray[CheckItem]
            CheckItem=CheckItem-1
            if CheckItem<0:
                LoopAgain=False
            elif IntegerArray[CheckItem]<=LastItem:
                LoopAgain=False
            IntegerArray[CheckItem+1]=LastItem
            NumberElements=NumberElements-1
        return IntegerArray
#Part cii
Sorted2Array=IterativeInsertion(NumberArray,len(NumberArray))
print("Iterative",NumberArray)
#Part ciii
#Part di
def BinarySearch(IntegerArray,First,Last,ToFind):
    if First>Last:
        return -1
    else:
        Middle=int((Last+First)/2)
        if IntegerArray[Middle]==ToFind:
            return Middle
        elif IntegerArray[Middle]>ToFind:
            Last=Middle-1
            return BinarySearch(IntegerArray,First,Last,ToFind)
        else:
            First=Middle+1
            return BinarySearch(IntegerArray,First,Last,ToFind)
#dii
Position=BinarySearch(Sorted2Array,0,len(NumberArray)-1,644)
if Position==-1:
    print("NotFound")
else:
    print(Position)
#Part diii

