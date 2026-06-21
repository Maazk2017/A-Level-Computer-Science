num=int(input("Enter the number: "))
print(num) 
#if we print a string there will be an error
#file=open("High.txt","r")
#print(file.read())
#file does not exist so error

#Exception Handling code
try:
    num=int(input("Enter a number: "))
    temp=num+2
    print(temp)
except:
    print("Invalid Datatype,make sure it's a number")
#Exception Handling in Files
try:
    nmu=5/0
    print(num)
    file=open("High.txt","r")
    print(file.read())
except IOError:
    print("File Does Not Exist,Make Sure To Use The Correct File Name")

#we have different exceptions
#if you to use it as a general exception then it will deal with all of the exception
#if you want to specify it to one exception only then you are supposed to mention that then it will only show that specific error ignore the others
#specify exception

try:
    nmu=5/0
    print(num)
    file=open("High.txt","r")
    print(file.read())
except ZeroDivisionError:
    print("Can't divide by zero")

#tackling both errors

try:
    file=open("High.txt","r")
    print(file.read())
except IOError:
    print("Wrong File")
try:
    num=5/0
    print(num)
except ZeroDivisionError:
    print("can't divide by zero") 

#PPQ
try:
    file=open("Progress.txt","r")
    gamedata=file.read()
except IOError:
    print("Incorrect File Name or File Does't Exists")