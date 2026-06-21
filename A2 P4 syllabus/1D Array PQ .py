#Q
array=[5,10,15,20,25,15]
print(array)
print(array[2])
#Q
sum=0
for x in range(len(array)):
    sum=sum+array[x]
print(sum)
count=0
#Q
for x in range (len(array)):
    if array[x]==15:
        count=count+1
        array[x]=""     
print(count)
print(array)
# PRACTICE QUESTION 
Name=["Taha","Ahmed","Pappo","Bano","Banto","Pappan"]
user=input("Please enter a name:")
flag=False
for x in range(len(Name)):
    if Name[x]==user:
        flag=True
        print("Not found")
if flag==False:
    Name.append(user)
    print(Name)

x=0
user=input("Please enter a name:")   
while x<len(Name) and flag==False:
    if Name[x]==user:
        flag=True   
    x=x+1    
if flag==False:
    Name.append(user)
    print(Name)
else:
    print("Not found")
#PRCTICE QUESTION
#flag=False
#sum=0
#count=0
#while flag==False:
    #num=float(input("Enter a number:"))
   #if num==0:
        #Flag=True
    #else:
        #sum=sum+num
        #count=count+1
#avg=sum/count
#print("Your average is",avg)

#PRACTICE QUESTION
Numbers=[10,32,24,56,75,86]
new=[0,0,0,0,0,0]
opposite_index=5
for index in range(len(Numbers)):
    new[index]=Numbers[opposite_index]
    opposite_index=opposite_index-1
print(new)


        

    


