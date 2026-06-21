class Human():
    def __init__(self,numheart):
        self._numeyes=2
        self._numeyes=1
        self._numnose=2
        self._numheart=numheart
    def eat(self):
        print("I Can Eat")
    def Work(self):
        print("I Can Work")
class Male(Human):
    def __init__(self,name,numheart):
        super().__init__(numheart)
        self._name=name 
    def Rizz(self):
        print("I Can Flirt")
    #Overirde
    def Work(self):
        super().Work() #it will print both the work method
        print("I Can Code")


male_1=Male("Maaz",1)
male_1.Rizz()
male_1.eat()
male_1.Work()
print(male_1._numnose)
print(male_1._numeyes)
print(male_1._numheart)

