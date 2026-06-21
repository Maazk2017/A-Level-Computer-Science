# Functions Practice
def table(number):
    count=0
    for x in range(11):
        temp=number*count
        print(str(number)+ " " + "x" + " " + str(count) + " " + "=" + " " +str(temp))
        count=count+1 
val=int(input("Enter a number"))
table(val)

# Part B
Number=[45,34,23,87,96,23]
def find(numarray):
    largestnumber=numarray[0]
    for x in range(len(numarray)):
        if numarray[x]>largestnumber:
            largestnumber=numarray[x]
    return largestnumber
temp_1=find(Number)
table(temp_1)
    
name=["Taha","Ahmed","Qasim"]
def linearsearch(array,find):
    for x in range(len(array)):
        if array[x]=="Ahmed":
            temp_2="The index value is:",x
    return temp_2
var=linearsearch(name,"Ahmed")
print (var)
    

