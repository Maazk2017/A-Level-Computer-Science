#While loop practice
x=0
while x <10:
    print("Hello")
    x=x+1   
print("Outside")

#FLAG LOOPING
flag=True
sum=0
while flag==True:# double== is for comparison and = is for assignment
    num=float(input("Please enter a number:"))
    if num==0:
        flag=False
    else:
        sum=sum+num
print("The sum is",sum)

#DIV & MOD
div=19//3 # Gives integer answer
print(div)
mod=10%3
print(mod)

#Practice Question
Div=11//2
print(Div)
Mod=11%2
print(Mod) 
#Mod means remainder 
#Div means Divisor or divided by 