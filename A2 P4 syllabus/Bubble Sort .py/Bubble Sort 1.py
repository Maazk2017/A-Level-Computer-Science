#Bubble Sort 
#How to swap variables
x=5
y=2
print("The value of x is",x)
print("The value is y is",y)

#Incorrect Method
#x=y
#y=x
#print("The value of x is",x)
#print("The value is y is",y)

#Correct Method
temp=x
x=y
y=temp
print("The value of x is",x)
print("The value is y is",y)

#How to swap elements in array
Number=[3,4]
#Incorrect Method
#Number[0]=Number[1]
#Number[1]=Number[0]

#Correct Method
w=0
temp_1=Number[w]
Number[w]=Number[1]
Number[w+1]=temp_1
print("The value of 0 is",Number[0])
print("The value of 1 is",Number[1])

#Bubble Sort Code
#Inefficient Code
#array=[10,5,6,7,1,12,13,15,21,8]
#def BubbleSort():
    #for x in range(len(array)):
        #for y in range((len(array))-1):
            #if array[y]>array[y+1]:
                #temp_2=array[y]
                #array[y]=array[y+1]
                #array[y+1]=temp_2
#BubbleSort()
#print(array) 

#Efficient Code
array=[10,5,6,7,1,12,13,15,21,8]

def BubbleSort():
    noswap=False
    boundary=9
    while noswap==False:
        noswap=True
        for y in range(boundary):
            if array[y]>array[y+1]:
                temp_2=array[y]
                array[y]=array[y+1]
                array[y+1]=temp_2
                noswap=False
        boundary=boundary-1
BubbleSort()
print(array)
#If we want to arrangr the array in descending order then just change the > to <


