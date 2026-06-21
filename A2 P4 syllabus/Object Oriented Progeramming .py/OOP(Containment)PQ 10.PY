#Containment Questions
#Q1
class fooditems():
    #PRIVATE name:STRING
    #PRIVATE code:STRING
    #PRIVATE cost:REAL
    def __init__(self,namep,codep,costp):
        self.__name=namep
        self.__code=codep
        self.__cost=costp
    def Getcode(self):
        return self.__code
    def Getcost(self):
        return self.__cost
    def Getname(self):
        return self.__name
class vendingMachine():
    #DECLARE items: ARRAY[0:3] OF fooditems
    #PRIVATE moneyIn:REAL
    def __init__(self,item1,item2,item3,item4):
        #self.__items=[]
        #self.__items.append[item1]
        #self.__items.append[item2]
        #self.__items.append[item3]
        #self.__items.append[item4]
        #another method
        self.__items=[0]*4
        self.__items[0]=item1
        self.__items[1]=item2
        self.__items[2]=item3
        self.__items[3]=item4
        self.__moneyIn=0
    def checkValid(self,code):
        for x in range(len(self.__items)):
            if self.__items[x].Getcode()==code:
                if self.__moneyIn>=self.__items[x].Getcost():
                    return x
                else:
                    return -2
            else:
                return -1
    def insertmoney(self,money):
        self.__moneyIn=money

chocolate=fooditems("You","1024",150.5)
sweets=fooditems("Lab-e-shiri","2817",12.2)
sandwich=fooditems("BBQ","2132",32.2)
apple=fooditems("red","4321",32.1)

machineone=vendingMachine(chocolate,sweets,sandwich,apple)
machineone.insertmoney(250.3)
temp=machineone.checkValid("1024")
print(temp)


    
    
    





        
        
