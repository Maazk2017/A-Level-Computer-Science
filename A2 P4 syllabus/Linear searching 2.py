#STRING MANIPULATION
name="papersdock"
print(name[0])
print(name[1])
print(name[9])
print(name[0:5]) # uptil 6 but not including 6
print(name[6:10])
var=name[3:6]
print(var)
#Practice Question
name_1="Taha Ali"
temp="The first name is"+ " "+name_1[0:4]
temp_1="The second name is"+" "+name_1[5:8]
print(temp+" "+temp_1)
#Lenght of a string
newname="Maaz Khan"
temp_2=len(newname)
print(temp_2)
#Practice Question
Name=input("Enter a name:")
for x in range(len(Name)):
    if Name[x]==" ":
           temp_3=x
           break
first=Name[0:temp_3]
last=Name[temp_3 + 1 : len(Name)]
print(first)
print(last)

#using while loop
x=0
falg=False
while falg ==False:
    if Name[x]==" ":
        wigga=x
        falg=True
    else:
        x=x+1
first=Name[0:wigga]
last=Name[wigga + 1 : len(Name)]
print(first)
print(last)

  