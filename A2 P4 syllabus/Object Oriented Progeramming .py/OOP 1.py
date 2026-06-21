#Object Oriented Programming
#How to make a CLASS and how to declare METHOD & Attributes
class Player():
    #PUBLIC name :STRING
    #PUBLIC age :INTEGER
    def __init__(self,Playername,Playerage):  #making constructor
        self.name=Playername   #PUBLIC attributes as self.name not self.__name
        self.age=Playerage     #PUBLUC attributes as self.name not self.__name
    #making METHOD
    def DisplayName(self):
        return self.name
    def getage(self):
        return self.age
#OBJECT creation
#making 2 OBJECTS
p1=Player("Ghost",21)
p2=Player("Ninga",19)
temp=p1.name
print(temp)

p1.name="Maaz"
temp_1=p1.name
print(temp_1)
print(p2.name,p2.age)
#using METHODS in OBJECT creation (PUBLIC)
temp_2=p2.DisplayName()
print(temp_2)
temp_3=p1.getage()
print(temp_3)


#Using Private ATTRIBUTES
class Player():
    #PUBLIC name :STRING
    #PUBLIC age :INTEGER
    def __init__(self,Playername,Playerage):  #making constructor
        self.__name=Playername   #PPRIVATE attributes as self.__name not self.name
        self.__age=Playerage     #PRIVATE attributes as self.__name not self.name
    #making METHOD
    def DisplayName(self):
        return self.__name
    def getage(self):
        return self.__age
#OBJECT creation
#making 2 OBJECTS
p1=Player("Ghost",21)
p2=Player("Ninga",19)
#using METHODS in OBJECT creation (PRIVATE)
temp_4=p1.DisplayName()
print(temp_4)
temp=p1.getage()
print(temp)
temp=int(input("Enter a Number"))