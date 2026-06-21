#Part a
# DECLARE numData : ARRAY [0 : 9] OF INTEGER

numData = [10, 4, 23, 45, 12, 8, 21, 11, 3, 1]
#Part bi
#we can not take parameter by reference so that's why taken as global
def BubbleSort():
    # DECLARE Noswaps : Boolean
    # DECLARE y, temp : INTEGER
    global numData
    Noswaps = False
    Boundary = 9
    while Noswaps == False:
        Noswaps = True
        for y in range(Boundary):
            if numData[y] > numData[y + 1]:
                temp = numData[y]
                numData[y] = numData[y + 1]
                numData[y + 1] = temp
                Noswaps = False
        Boundary = Boundary - 1
#Part bii
BubbleSort()
print(numData)
#Part ci
def EvenNumber(Array):
    count=0
    for x in range(len(Array)):
        if x%2==0:
            count=count+1
    return count
#Part cii
Temp=EvenNumber(numData)
print("There are",Temp,"even numbers")
#Part ciii
