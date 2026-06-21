#Part a
#DECLARE Animals:ARRAY[0:9]OF STRING
global Animals
Animals=[]
#Part b
Animals.append("horse")
Animals.append("lion")
Animals.append("rabbit")
Animals.append("mouse")
Animals.append("bird")
Animals.append("deer")
Animals.append("whale")
Animals.append("elephant")
Animals.append("kangaroo")
Animals.append("tiger")
#Part c
def SortDescending():
    ArrayLength=len(Animals)
    for x in range(0,ArrayLength):
        for y in range(0,ArrayLength-x-1):
            if Animals[y][0:1]<Animals[y+1][0:1]:
                Temp=Animals[y]
                Animals[y]=Animals[y+1]
                Animals[y+1]=Temp
#Part di
SortDescending()
for x in range(10):
    print(Animals[x])
#Part dii