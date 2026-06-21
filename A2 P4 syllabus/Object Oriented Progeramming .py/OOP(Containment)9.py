class Engine():
    def __init__(self, power):
        self.__power = power
    
    def SpeedIncrease(self):
        print("Speeding UP", self.__power)

#We have created two different engines        
BMWEngine = Engine(900)
FerrariEngine = Engine(70)

# Airplane class contains two engines object
class Airplane():
    def __init__(self, model, engine, engine2):
        self.__Model = model
        self.__Engine = engine # Containment Engine Exists inside Airplane
        self.__Engine2 = engine2

    def StartEngine(self):
        print("Engine is Starting")
        self.__Engine.SpeedIncrease() #BMWEngine.SpeedIncrease()
        self.__Engine2.SpeedIncrease() #FerrariEngine.SpeedIncrease()
    
MeraJahaz = Airplane("PIAA009", BMWEngine, FerrariEngine)

MeraJahaz.StartEngine()
