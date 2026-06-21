class foodItem():
    # PRIVATE name : STRING
    # PRIVATE code : STRING
    # PRIVATE cost : REAL

    def __init__(self, nameP, codeP, costP):
        self.__name = nameP
        self.__code = codeP
        self.__cost = costP

    def getCode(self):
        return self.__code

    def getCost(self):
        return self.__cost

    def getName(self):
        return self.__name

class vendingMachine():
    # PRIVATE items : ARRAY[0:3] OF foodItem
    # PRIVATE moneyIn : REAL

    def __init__(self, item1, item2, item3, item4):
        self.__moneyIn = 0
        self.__items = [0] * 10
        self.__items[0] = item1  # You can use the concept of Append aswell
        self.__items[1] = item2
        self.__items[2] = item3
        self.__items[3] = item4

    def checkValid(self, code):
        for x in range(4):
            if self.__items[x].getCode() == code:
                if self.__items[x].getCode() <= self.__moneyIn:
                    return x
                else:
                    return -2
        return -1

    def getItemName(self, index):
        temp = self.__items[index].getName()
        return temp


chocolate = foodItem("Oreo", 54, 5.4)
sweets = foodItem("Custard", 12, 2.1)
sandwich = foodItem("Peri Peri", 67, 10.1)
apple = foodItem("green", 3, 1.3)


machineOne = vendingMachine(chocolate, sweets, sandwich, apple)

itemname = machineOne.getItemName(2)
print(itemname)


