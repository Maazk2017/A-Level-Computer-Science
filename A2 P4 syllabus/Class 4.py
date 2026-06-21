#LOOPS
for x in range(1,11):
    print(x)

#PRACTICE QUESTION 
for x in range(10):
    temp=input("Please enter name:")
    print("Good Morning"+" "+temp)

#SUM TECHNIQUE
#practice question
sum=0
for x in range(5):
    num=float(input("Enter a number"))
    sum=sum+num
print("your sum is",sum)

#Large Technique
#practice question
large=9999
for x in range(5):
    number=float(input("Enter a number:"))
    if number>large:
        large=number
print(large)    

#Count Technique
#practice question
for x in range(5):
    num_1=float(input("Enter number:"))
    count=count+1
print("The count is",count)

#practice question
poscount=0
negcount=0
for x in range(5):
    num_2=float(input("Enter a number:"))
    if num_2>0:
        poscount=poscount+1
    else:
        negcount=negcount+1
print(poscount,"Positive numbers")
print(negcount,"Negative number")



#Small Technique
#practice question
small=0
for x in range(5):
    num_3=float(input("Enter a number:"))
    if num_3<small:
        small=num_3
print(small)

#While Loop
#Practice Question
sum=0
x=0
while x<5:
    num_4=float(input("Enter a number:"))
    sum=sum+num_4
    x=x+1
print(sum)


