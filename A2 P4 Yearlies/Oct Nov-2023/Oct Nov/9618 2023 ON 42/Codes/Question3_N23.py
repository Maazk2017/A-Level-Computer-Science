import datetime

class Character():
    #PRIVATE CharacterName : STRING
    #PRIVATE DateOfBirth : DATE
    #PRIVATE Intelligence : REAL
    #PRIVATE Speed : INTEGER

    def __init__(self, CharacterNameP, DateOfBirthP, IntelligenceP, SpeedP):
        self.__CharacterName = CharacterNameP
        self.__DateOfBirth = DateOfBirthP
        self.__Intelligence = IntelligenceP
        self.__Speed = SpeedP

    def GetIntelligence(self):
        return self.__Intelligence

    def GetName(self):
        return self.__CharacterName

    def SetIntelligence(self, NewIntelligenceP):
        self.__Intelligence = NewIntelligenceP

    def Learn(self):
        self.__Intelligence = self.__Intelligence + (self.__Intelligence * 0.1)

    def ReturnAge(self):
        Age = 2023 - self.__DateOfBirth.year
        return Age


class MagicCharacter(Character):
    #PRIVATE Element : STRING
    def __init__(self, CharacterNameP, DateOfBirthP, IntelligenceP, SpeedP, ElementP):
        super().__init__(CharacterNameP, DateOfBirthP, IntelligenceP, SpeedP)
        self.__Element = ElementP

    def Learn(self):
        if self.__Element == "fire" or self.__Element == "water":
            newintelligence = super().GetIntelligence() + (super().GetIntelligence() * 0.2)
        elif self.__Element == "earth":
            newintelligence = super().GetIntelligence() + (super().GetIntelligence() * 0.3)
        else:
            newintelligence = super().GetIntelligence() + (super().GetIntelligence() * 0.1)

        super().SetIntelligence(newintelligence)




FirstCharacter = Character("Royal", datetime.datetime(2019, 1, 1), 70.0, 30)
FirstCharacter.Learn()
Name = FirstCharacter.GetName()
Age = FirstCharacter.ReturnAge()
Intelligence = FirstCharacter.GetIntelligence()
print(Name, "is", Age, "years old and his intelligence is", Intelligence)


FirstMagic = MagicCharacter("Light", datetime.datetime(2018, 3, 3), 75.0, 22, "fire")
FirstMagic.Learn()
Name2 = FirstMagic.GetName()
Age2 = FirstMagic.ReturnAge()
Intelligence2 = FirstMagic.GetIntelligence()
print(Name2, "is", Age2, "years old and his intelligence is", Intelligence2)
