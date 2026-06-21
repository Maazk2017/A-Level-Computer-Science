def IterativeVowels(Value):
    Total=0
    LenghtString=len(Value)
    for x in range(0,LenghtString):
        FirstCharcter=Value[0]
        if FirstCharcter=="a" or FirstCharcter=="e" or FirstCharcter=="i" or FirstCharcter=="o" or FirstCharcter=="u":
            Total=Total+1
        Value=Value[1:len(Value)]
        print(Value)
        print(LenghtString)
    return Total
temp=IterativeVowels("house")
print("Iterative",temp)

#Part b
def RecursiveVowels(Value):
    #Base Case
    if len(Value)==0:
        return 0 #Means Total=0
    #General Case
    else:
        FirstCharacter=Value[0]
        if FirstCharacter=="a" or FirstCharacter=="e" or FirstCharacter=="i" or FirstCharacter=="o" or FirstCharacter=="u":
            Value=Value[1:len(Value)]
            return RecursiveVowels(Value)+1
        else:
            Value=Value[1:len(Value)]
            return RecursiveVowels(Value)+0
RecursiveOutput=RecursiveVowels("house") 
print("Recursive",RecursiveOutput)


















#STEPS TO WRITE ITERATIVE TO RECURSIVE

#Step1:Understand the iterative code by dry run
#Step2:Figure out the base case
#      by seeing the loops condition
#Step3:Figure out the calculation
#Step4:Count=0 return 0 in base case
#      Total=1 return 1 in base case
#Step5:Calculion should be done recursive calls
#      count=count+1
#      return recursivecount(index+1)+1
#
#      Total=Total+num
#      return recursivenum(index+1)+num

#Linking Concepts 
#In Iteration every loop the value is cahnging
#house
#ouse
#use
#se
#e
# ...

#In Every Recursion
#Recursion("House")
#Recursion("ouse")
#Recursion("use")
#Recursion("se")
#Recursion("e")
#Recursion("")

#Base Case
#if len(Value)==0:

#Initailization in iterative code
#Ttoal=0
#In Recursion the initialization will be done in base case with return

#if len(Value)==0:
#return 0

#Total=Total +1     in recursion will be
#recursive(Value)+1



       