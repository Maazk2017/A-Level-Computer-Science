#Linked List
class Node():
    #PUBLIC Data:STRING
    #PUBLIC Pointer:INTEGER
    def __init__(self,Data,Pointer):
        self.Data=Data
        self.Pointer=Pointer
StartPointer=0
LinkedList=[Node("A",2),Node("C",3),Node("B",1),Node("D",-1),Node("",-1)]
tempdata=LinkedList[3].Data
print(tempdata)
templocation=LinkedList[StartPointer].Pointer #This is 3 ki location
print(LinkedList[templocation].Data)
newlocation=LinkedList[templocation].Pointer
print(LinkedList[newlocation].Data)
nextnodelocation=LinkedList[newlocation].Pointer
print(LinkedList[nextnodelocation].Data)

