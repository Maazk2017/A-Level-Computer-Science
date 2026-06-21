#ARRAYS
Name=["Taha","Ahmed","Pappo","Bano","Banto","Pappan"]
#        0       1       2      3      4        5     
print(Name[0])
print(Name[1])
#Finding length of names
#LENGTH NAMES
Length=len(Name)
print(Length)
#Length function in loop
#Find the index position of bano
#LINEAR SEARCHING
for index in range(len(Name)):
    if Name[index]=="Bano":
        print(index)
#USING WHILE LOOP
x=0
flag=False
while x<len(Name) and flag==False:
    if Name[x]=="Jhon":
        print(x)
        flag=True
    else:
        x=x+1
if flag==False: #if not flag:
    print("not found")
#Adding items in the list
#Q add one more name in the array
#Names.append("Maaz")
Name.append("Maaz")
print(Name)

mod=False
for x in range(len(Name)):
    if Name[x]=="Maaz":
        print(x)
        mod=True
        break
if mod==False:
    print("Not Found")


Numbers=[10,32,24,56,75,86]
new=[0,0,0,0,0,0]
opposite_index=5
for index in range(len(Numbers)):
    new[index]=Numbers[opposite_index]
    opposite_index=opposite_index-1
print(new)
