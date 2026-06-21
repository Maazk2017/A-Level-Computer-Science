class Box():
    # PRIVATE Size : STRING
    # PRIVATE Contents : ARRAY[0:9] OF FieldObject
    # PRIVATE Lock : STRING
    # PRIVATE Strength : INTEGER

    def __init__(self, SizeP, LockP, FirstContentP):
        self.__Contents = [0] * 10
        self.__Size = SizeP
        self.__Lock = LockP
        self.__Strength = 100
        self.__Contents[0] = FirstContentP

    def Unlock(self, code):
        if self.__Lock == code:
            return True
        else:
            self.__Strength = self.__Strength - 1
            if self.__Strength <= 0:
                return True
            else:
                return False

    def getContent(self):
        return self.__Contents

    def setSize(self, newSize):
        self.__Size = newSize

    def setContents(self, array):
        self.__Contents = array

    def setLock(self, newLock):
        self.__Lock = newLock

    def setStrength(self, newStrength):
        self.__Strength = newStrength


