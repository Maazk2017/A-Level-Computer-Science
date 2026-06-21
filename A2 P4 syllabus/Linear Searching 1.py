#LINEAR SEARCHING
Number=[23,12,34,41,45,65,-2,-4,-1,-7]
for x in range(len(Number)):
    if Number[x]==41:
        print("The Index Value Of 41 is:",x)
#Make a fuction posnegcount which will take array as the parameter and then calculate and then return a string and then return a appropirate string telling the count
def posnegcount(Number_1):
    poscount=0
    negcount=0
    for x in range(len(Number_1)):
        if Number_1[x]>0:
            poscount=poscount+1 
        elif Number_1[x]<0:
            negcount=negcount+1
    temp="Positive numbers are"+" "+str(poscount)+" "+"Negative numbers are"+" "+str(negcount)
    return (temp)
countstr=posnegcount(Number)
print(countstr)

#PRACTICE QUESTION
name=["Taha","Ahmed","Qasim"]
def linearsearch(array,find):
    for x in range(len(array)):
        if array[x]==find:
            temp_2="The index value is"+" "+str(x)
    return temp_2
var=linearsearch(name,"Ahmed")
print (var)


       




