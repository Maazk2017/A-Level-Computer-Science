#Part ai
class FoodItem():
    #PRIVATE Name:STRING
    #PRIVATE Code:STRING
    #PRIVATE Cost:REAL
    def __init__(self,Name,Code,Cost):
        self.__Name=Name
        self.__Code=Code
        self.__Cost=Cost
#Part aii
    def GetName(self):
        return self.__Name
    def GetCode(self):
        return self.__Code
    def GetCost(self):
        return self.__Cost
#Part bi
class VendingMachine():
    #PRIVATE Items:ARRAY[0:3] OF FoodItem
    #PRIVATE MoneyIn:REAL
    def __init__(self,Item1,Item2,Item3,Item4):
        self.__Items=[]
        self.__Items.append(Item1)
        self.__Items.append(Item2)
        self.__Items.append(Item3)
        self.__Items.append(Item4)
        self.__MoneyIn=0
#Part bii
    def CheckValid(self,Code):
        for x in range(len(self.__Items)):
            if self.__Items[x]==Code:
                if self.__MoneyIn<self.__Items[x].GetCode():
                    return -2
                elif self.__MoneyIn>=self.__Items[x].GetCode():
                    return x
            else:
                return -1
#Part biv
    def GetItemName(self,index):
        Temp=(self.__Items[index].GetName())
        return Temp
#Part biii
chocolate = FoodItem("Oreo", 54, 5.4)
sweets = FoodItem("Custard", 12, 2.1)
sandwich = FoodItem("Peri Peri", 67, 10.1)
apple = FoodItem("green", 3, 1.3)
machineOne = VendingMachine(chocolate, sweets, sandwich, apple)
print(machineOne.GetItemName(2))

            




    