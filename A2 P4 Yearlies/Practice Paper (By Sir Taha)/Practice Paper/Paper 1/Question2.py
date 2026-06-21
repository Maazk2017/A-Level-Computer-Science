#Part a
class Box():
    #PRIVATE Size:STRING 
    #PRIVATE Contents:ARRAY[0:9]OF FieldObject
    #PRIVATE Lock:STRING
    #PRIVATE Strength:INTEGER
    def __init__(self,Size,Content1,Lock):
        self.__Size=Size
        self.__Contents=[0]*10
        self.__Contents[0]=Content1
        self.__Lock=Lock
        self.__Strength=100
#Part b
    def unlock(self,Code):
        if Code==self.__Lock:
            return True
        else:
            self.__Strength=self.__Strength-1
            if self.__Strength<1:
                return True
            else:
                return False
#Part ci
    def GetContents(self):
        return self.__Contents
#Part cii
    def SetSize(self,NewSize):
        self.__Size=NewSize
    def SetContents(self,NewContents):
        self.__Contents=NewContents
    def SetLock(self,NewLock):
        self.__Lock=NewLock
    def SetStrength(self,NewStrength):
        self.__Strength=NewStrength


