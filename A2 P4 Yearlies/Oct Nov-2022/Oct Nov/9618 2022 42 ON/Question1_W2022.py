#Part a
#DECLARE Jobs:ARRAY[0:99,0:1]OF INTEGER
global NumberOfJobs
global Jobs
NumberOfJobs=0
Jobs=[[0]*2 for i in range(100)]
#Part b
def Initialize():
    global Jobs
    for i in range(100):
        Jobs[i][0]=-1
        Jobs[i][1]=-1
    NumberOfJobs=0
#part c
def AddJob(Number,Priority):
    global Jobs
    global NumberOfJobs
    if NumberOfJobs<100:
        Jobs[NumberOfJobs][0]=Number
        Jobs[NumberOfJobs][1]=Priority
        NumberOfJobs=NumberOfJobs+1
        print("Added")
    else:
        print("Not Added")
#Part d
Initialize()
AddJob(12,10)
AddJob(526,9)
AddJob(33,8)
AddJob(12,9)
AddJob(78,1)
#Part e
def InsertionSort():
    global Jobs
    global NumberOfJobs

    # Array Size Is NumberOfJobs

    for pointer in range(1, NumberOfJobs):
        ValueJob = Jobs[pointer][0]
        ValuePriority = Jobs[pointer][1]

        #holeposition is the index that we are trying to find
        #which is basically the correct position 

        holeposition = pointer

        while holeposition > 0 and Jobs[holeposition - 1][1] > ValuePriority:
            Jobs[holeposition][0] = Jobs[holeposition - 1][0]
            Jobs[holeposition][1] = Jobs[holeposition - 1][1]
            holeposition = holeposition -1

        Jobs[holeposition][0] = ValueJob
        Jobs[holeposition][1] = ValuePriority
#Part f
def PrintArray():
    global Jobs
    global NumberOfJobs
    for i in range(NumberOfJobs):
        print(str(Jobs[i][0])+" "+"Priority"+" "+str(Jobs[i][1]))
#Part gi
InsertionSort()
PrintArray()
#Part gii







