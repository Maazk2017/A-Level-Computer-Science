#Session 5 INSERTION SORT

# DECLARE Jobs : ARRAY[0:99, 0:1] OF INTEGER
# DECALRE NumOfJobs : INTEGER
global Jobs
global NumberOfJobs
Jobs = []

def Initialise():
    global Jobs
    global NumberOfJobs
    NumberOfJobs = 0
    for x in range(100):
        Jobs.append([-1, -1])


def AddJob(JobNumber, Priority):
    global Jobs
    global NumberOfJobs

    if NumberOfJobs < 100:
        Jobs[NumberOfJobs][0] = JobNumber
        Jobs[NumberOfJobs][1] = Priority
        #Jobs[NumofJObs] = [JobNumber, Priority]
        print("Added")
        NumberOfJobs = NumberOfJobs + 1
    else:
        print("Not Added")

Initialise()

AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)


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


def PrintArray():
    global Jobs
    global NumberOfJobs

    for rows in range(NumberOfJobs):
        Job = Jobs[rows][0]
        priority = Jobs[rows][1]

        line = str(Job) + " " + "priority" + " " + str(priority)
        print(line)

InsertionSort()
PrintArray()



 

        


        


  


            
            