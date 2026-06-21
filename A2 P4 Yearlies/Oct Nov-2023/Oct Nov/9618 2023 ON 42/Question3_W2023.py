import datetime
#Part ai
class Character():
    #PRIVATE CharacterName:STRING
    #PRIVATE DateOfBirth:DATE   
    #PRIVATE Intelligence:REAL
    #PRIVATE Speed:INTEGER
    def __init__(self,CharacterName,DateOfBirth,Intelligence,Speed):
        self.__CharacterName=CharacterName
        self.__DateOfBirth=DateOfBirth
        self.__Intelligence=Intelligence
        self.__Speed=Speed
#Part aii
    def GetIntelligence(self):
        return self.__Intelligence
    def GetName(self):
        return self.__CharacterName
#Part aiii
    def SetIntelligence(self,NewIntellignece):
        self.__Intelligence=NewIntellignece
#Part aiv
    def Learn(self):
        self.__Intelligence=self.__Intelligence+self.__Intelligence*0.1
#Part v 
    def ReturnAge(self):
        Age=2023-self.__DateOfBirth.year
        return Age
#Part bi
print("Character")
FirstCharacter=Character("Royal",datetime.datetime(2019,1,1),70,30)
#Part bii
FirstCharacter.Learn()
print("The Name is",FirstCharacter.GetName(),"The Age is",FirstCharacter.ReturnAge(),"The Itelligence is",FirstCharacter.GetIntelligence())
#Part ci
class MagicCharacter(Character):
    #PRIVATE Element:STRING
    def __init__(self,Element,CharacterName,DateOfBirth,Intelligence,Speed):
        super().__init__(CharacterName,DateOfBirth,Intelligence,Speed)
        self.__Element=Element
#Partii
    def Learn(self):
        if self.__Element=="water" or self.__Element=="fire":
            newintel=super().GetIntelligence()+(super().GetIntelligence()*0.2)
        elif self.__Element=="earth":
            newintel=super().GetIntelligence()+(super().GetIntelligence()*0.3)
        else:
            newintel=super().Learn()
#Part di
FirstMagic=MagicCharacter("fire","Light",datetime.datetime(2018,3,3),75,22)
print("Magic Character")
FirstMagic.Learn()
Name=FirstMagic.GetName()
Age=FirstMagic.ReturnAge()
Intel=FirstMagic.GetIntelligence()
print("The name is",Name,"Age is",Age,"Intelligence is",Intel)



