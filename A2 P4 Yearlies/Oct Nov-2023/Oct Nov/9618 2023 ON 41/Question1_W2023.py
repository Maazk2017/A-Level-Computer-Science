#Part ai
def IterativeVowels(Value):
    Total=0
    LenghtString=len(Value)
    for x in range(0,LenghtString):
        FirstCharacter=Value[0]
        if FirstCharacter=="a" or FirstCharacter=="e" or FirstCharacter=="i" or FirstCharacter=="o" or FirstCharacter=="u":
            Total=Total+1
        Value=Value[1:LenghtString]
    return Total
#Part aii
Temp=IterativeVowels("house")
print("Iterative",Temp)
#Part aiii
#Part bi
def RecursiveVowels(Value):
    if len(Value)==0:
        return 0
    else:
        FirstCharacter=Value[0]
        if FirstCharacter=="a" or FirstCharacter=="e" or FirstCharacter=="i" or FirstCharacter=="o" or FirstCharacter=="u":
            Value = Value[1: len(Value)]
            return 1 + RecursiveVowels(Value)
        else:
            Value = Value[1: len(Value)]
            return 0 + RecursiveVowels(Value)
#Part bii
Temp=RecursiveVowels("imagine")
print("Recursive",Temp)
#Part biii



        

