#Insertion Sort
#Code
arraydata=[10,5,6,7,1]

def InsertionSort():
    arraysize=len(arraydata) #5 elements
    #we are starting from 1 because wer are considering 0 is alredy sorted
    for pointer in range(1,arraysize):
        valuetoinsert=arraydata[pointer] #so we don't loose array value
        holeposition=pointer #Index value 
        while(holeposition>0) and arraydata[holeposition-1]>valuetoinsert:
            #Shifting
            #H.p -1
            arraydata[holeposition]= arraydata[holeposition-1]
            holeposition=holeposition-1
        arraydata[holeposition]=valuetoinsert

InsertionSort()
print(arraydata)

           
