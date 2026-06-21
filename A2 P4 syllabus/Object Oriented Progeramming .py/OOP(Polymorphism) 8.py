#Concept Of Polymorphism
class Animal():
    def Awaaz(self):
        print("Animal Voice")
class Kutta(Animal):
    def Awaaz(self):
        super().Awaaz()
        print("Bhao Bhao")
class Billi(Animal):
    def Awaaz(self):
        super().Awaaz()
        print("Meow Meow")

Tommy=Kutta()
Mano=Billi()

Mano.Awaaz()
Tommy.Awaaz()


