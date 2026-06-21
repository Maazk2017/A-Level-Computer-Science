#BUILT IN FUNCTIONS
#random
import random
x=random.randint(1,100)
print(x)
for i in range(10):
    x=random.randint(1,100)
    print(x)
#lenght
name="Maaz"
print(len(name))
#UpperCase
name="maaz"
print(name.upper())
#LowerCase
name="MAAZ"
print(name.lower())
#for e.g
userresponse=input("Enter yes or no:")
if userresponse.lower()=="yes":
    print("Working")
else:
    print("not working")
#Split
text="Hello Taha"
part=text.split()
print(part)
#the text is split into array
text="taha,ali,bano,ahmed"
parts=text.split(",") #can specify the seperator
print(parts[3])
for x in range(3):
    print(parts[x])
