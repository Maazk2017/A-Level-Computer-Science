import datetime
DateOfBirth=datetime.date(2007,2,10)
print(DateOfBirth.year)
print(DateOfBirth.month)
print(DateOfBirth.day)
#Question1
class Character():
#Part a
    #DECLARE PRIVATE CharacterName:STRING
    #DECLARE PRIVATE DateOfBirth:DATE
    #DECLARE PRIVATE Intelligence:INTEGER
    #DECLARE PRIVATE Speed:INTEGER
    def __init__(self,CharacterName,DateOfBirth,Intelligence,Speed):
        self.__CharacterName=CharacterName
        self.__DateOfBirth=DateOfBirth
        self.__Intelligence=Intelligence
        self.__Speed=Speed
#Part b
    def GetIntelligence(self):
        return self.__Intelligence
    def GetName(self):
        return self.__CharacterName
#Part c
    def SetIntelligence(self,NewIntelligence):
        self.__Intelligence=NewIntelligence
#Part d
    def Learn(self):
        increasedvalue=self.__Intelligence*0.1
        self.__Intelligence=self.__Intelligence+increasedvalue
        return self.__Intelligence
#Part e 
    def ReturnAge(self):
        CurrentYear=self.__DateOfBirth.year
        Age=2023-CurrentYear
        return Age
#Part f
FirstCharacter=Character("Royal",datetime.date(2019,1,1),70,30)
Name=FirstCharacter.GetName()
Age=FirstCharacter.ReturnAge()
Intel=FirstCharacter.Learn()
print("The Name is",Name,"The Age is",Age,"The Intelligence is",Intel)
#Part g
class MagicCharacter(Character):
    def __init__(self,CharacterName,DateOfbirth,Intelligence,Speed,Element):
        super().__init__(CharacterName,DateOfbirth,Intelligence,Speed)
        self.__Element=Element
#Part h
    def Learn(self):
        if self.__Element=="Fire" or self.__Element=="Water":
            increasedValue=super().GetIntelligence()*0.2
            NewIntelligence=super().GetIntelligence()+increasedValue
        elif self.__Element=="Earth":
            increasedValue=super().GetIntelligence()*0.3
            NewIntelligence=super().GetIntelligence()+increasedValue
        else:
            increasedValue=super().__GetIntelligence()*0.1
            NewIntelligence=super().GetIntelligence()+increasedValue
#Part i
FirstMagic=MagicCharacter("Light",datetime.date(2018,3,3),75,22,"Fire")
#Part j
FirstMagic.Learn()
Name=FirstMagic.GetName()
Age=FirstMagic.ReturnAge()
Intel=FirstMagic.GetIntelligence()
print("The Name is",Name,"The Age is",Age,"The Intelligence is",Intel)

