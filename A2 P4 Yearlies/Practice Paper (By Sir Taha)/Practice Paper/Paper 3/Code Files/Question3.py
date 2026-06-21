# DECLARE numData : ARRAY [0 : 9] OF INTEGER

numData = [10, 4, 23, 45, 12, 8, 21, 11, 3, 1]

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

BubbleSort()
print(numData)

def EvenNumber(arrayname):
    count = 0
    for x in range(len(arrayname)):
        if (x % 2) == 0:
            count = count + 1
    return count

Evencount = EvenNumber(numData)
print("Even Number Are:",Evencount)

