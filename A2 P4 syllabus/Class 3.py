#SELECTIONAL STATEMENT
number=float(input("Please enter a number: "))
if number>54:
    print("It is greater than 54")

#PRATICE QUESTION 
num=float(input("Please enter a number:"))
if num==20:
    print("sahi hai lekin uska number nahi jo khush ho rahe ho")
elif num==21:
    print("Not correct but close")
else:
    print("App se nahi ho pai ga")

#PRACTICE QUESTION
num_1=float(input("Please enter first number:"))
num_2=float(input("Please enter second number:"))
num_3=float(input("Please enter third number:"))
if num_1>num_2 and num_1>num_3:
    print("largest number is:",num_1)
elif num_2>num_1 and num_2>num_3:
    print("largest number is num_2:",num_2)
else:
    print("Largest number is:",num_3)

#PRACTICE QUESTION
mail=input("Please enter your email:")
pin=input("Please enter your password:")
if mail=="123@papersdock.com" and pin=="12ab":
    print("Successful login")
else:
    print("Incorrect information")