#Question 3 

global QueueData
global QueueHead
global QueueTail

QueueData = []
for x in range(20):
    QueueData.append("")

QueueHead = -1
QueueTail = -1

def Enqueue(DataToInsert):
    global QueueData
    global QueueHead
    global QueueTail

    if QueueTail == -1:
        QueueTail = 0
    
    if QueueTail < 20:
        if QueueHead == -1:
            QueueHead = 0
        
        QueueData[QueueTail] = DataToInsert
        QueueTail = QueueTail + 1
        return True
    else:
        return False

def Dequeue():
    global QueueData
    global QueueHead
    global QueueTail

    if QueueHead == -1:
        return "false"
    else:
        item = QueueData[QueueHead]
        QueueHead = QueueHead + 1
    
    if QueueHead == QueueTail:
        QueueTail = -1
        QueueHead = -1
    
    return item


def StoreItems():
    global QueueHead
    global QueueData
    global QueueTail

    invalidcount = 0

    for x in range(10):
        Data = input("Enter the Data: ")

        Total1 = int(Data[0]) + int(Data[2]) + int(Data[4])
        Total3 = (int(Data[1]) * 3) + (int(Data[3]) * 3) + (int(Data[5]) * 3)
        Total = Total1 + Total3
        CheckDigit = int(Total/10)

        if (CheckDigit == 10 and Data[6] == "X") or CheckDigit == int(Data[6]):
            Result = Enqueue(Data[0:6])

            if Result == True:
                print("Data Inserted")
            else:
                print("Queue is full")
        else:
            invalidcount = invalidcount + 1

    print("There were", invalidcount, "Invalid Items")



StoreItems()

flag = Dequeue()
if flag == "false":
    print("Queue is empty")
else:
    print("Dequeued Value: ",flag)
    
        
    
        
