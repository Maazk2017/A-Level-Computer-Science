

#Record data type is just a class with public attribute(no double score) object will be your record
class Book():
    #PUBLIC ISBN :INTEGER
    #PUBLIC Author :STRING
    #PUBLIC Genre :STRING
    def __init__(self,ISBN,Author,Genre):
        self.ISBN=ISBN
        self.Author=Author
        self.Genre=Genre
Book1=Book(12345,"Maaz","Mystrey")
print(Book1.Author)
Book1.Author="Shela Ki Jawani"
print(Book1.Author)
print(Book1.Genre)
#Q1
class Node():
    #PUBLIC data :INTEGER
    #PUBLIC nextNode :INTEGER
    def __init__(self,data,nextNode):
        self.data=data
        self.nextNode=nextNode
LinkedList=[Node(45,1),Node(34,2),Node(65,-1)]
print(LinkedList[0].nextNode)
print(LinkedList[2].data)
LinkedList[1].nextNode=8
print(LinkedList[1].nextNode)
#Concept
nextlocation=LinkedList[0].nextNode
print(LinkedList[nextlocation].data)






