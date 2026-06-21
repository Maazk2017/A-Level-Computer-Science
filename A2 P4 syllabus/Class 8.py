#2D ARRAY
Names=[["Ahmed","Ali","Bano"],["Qasim","Faisal","Jaun"]]
#Linear searching elements search each element
# Question if faisal is in the array print present and if not print not there 
flag=False
for rows in range(2):
    for col in range(3):
        if Names[rows][col]=="Ahmed":
            flag=True
if flag==False:
    print("Present")
else:
    print("Not there")
#CREATING ARRAYS USING LOOPS
emptyarray=["0"]*10
emptyarray[2]=45
print(emptyarray)

#ANOTHER WAY
EmptyArray=[]
for x in range(5):
    EmptyArray.append(0)
print(EmptyArray)
#Boolean Intialization
EmptyArray=[]
for x in range(5):
    EmptyArray.append(True)
print(EmptyArray)
#CREATING 2D ARRAYS USING LOOPS
Empty2D=[["2"]*4 for i in range(5)]
print(Empty2D)
for x in range(5):
    print(Empty2D[x])
New2D=[[10]*12 for i in range(25)]
print(New2D)


