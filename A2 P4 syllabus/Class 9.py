#FUCTIONS
def name():
    print("Maaz")
name()
#Greeting Fuction
def Greeting(name):
    combine="Hello"+" "+name
    print(combine)
Greeting("Maaz")
Greeting("Madison Beer")
#Create a function Morning in which take name and print good morning name
def Morning(name):
    temp="Good Morning"+" "+name
    print(temp)
Morning("Maaz")
Morning("Megan Fox")

def Average(sum,count):
    temp_1=sum/count
    print(temp_1)
Average(10,5)

# HOW TO USE RETURN
def Average(sum,count):
    temp_1=sum/count
    return temp_1
Answer=Average(120,3)
newans=Answer*2
print(newans)

def Grader(Score):
    if Score>=90:
        return "A"
    elif Score>=80:
        return "B"
    else:
        return "F"
Marks=float(input("Enter a number"))
var=Grader(Marks)
print("Your grade is",var)









