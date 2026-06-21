#Part ai
class EventItem():
    #PRIVATE EventName:STRING
    #PRIVATE Type:STRING
    #PRIVATE Difficulty:INTEGER
    def __init__(self,EventName,Type,Difficulty):
        self.__EventName=EventName
        self.__Type=Type
        self.__Difficulty=Difficulty
#Part aii
    def GetName(self):
        return self.__EventName
    def GetDifficulty(self):
        return self.__Difficulty
    def GetEventType(self):
        return self.__Type
#Part bi
#DECLARE Group:ARRAY [0:4] OF EventItem
Group=[]
#Part bii
Group.append(EventItem("Bridge","jump",3))
Group.append(EventItem("Water Wade","swim",3))
Group.append(EventItem("100 mile run","run",3))
Group.append(EventItem("Gridlock","drive",3))
Group.append(EventItem("Wall on Wall","jump",3))
#Part c
class Character():
    #PRIVATE CharacterName:STRING
    #PRIVATE Jump:INTEGER
    #PRIVATE Swim:INTEGER
    #PRIVATE Run:INTEGER
    #PRIVATE Drive:INTEGER
    def __init__(self,CharacterName,Jump,Swim,Run,Drive):
        self.__CharacterName=CharacterName
        self.__Jump=Jump
        self.__Swim=Swim
        self.__Run=Run
        self.__Drive=Drive
    def GetName(self):
        return self.__CharacterName
#Part d
    def CalculateScore(self,typevent,difficulty):
        if typevent=="jump":
            skilllevel=self.__Jump
        elif typevent=="swim":
            skilllevel=self.__Swim
        elif typevent=="run":
            skilllevel=self.__Run
        else:
            skilllevel=self.__Drive
        if skilllevel>=difficulty:
            return 100
        else:
            Temp=difficulty-skilllevel
            if Temp==1:
                return 80
            elif Temp==2:
                return 60
            elif Temp==3:
                return 40
            else:
                return 20 
#Part e
P1=Character("Tarz",5,3,5,1)
P2=Character("Geni",2,2,3,4)
#Part eii
P1Points=0
P2Points=0
for x in range(5):
    EventType=Group[x].GetEventType()
    Difficulty=Group[x].GetDifficulty()
    P1EventScore=P1.CalculateScore(EventType,Difficulty)
    P2EventScore=P2.CalculateScore(EventType,Difficulty)
    if P1EventScore>P2EventScore:
        P1Points=P1Points+1
        print(P1.GetName(),"you win this event")
    elif P2EventScore>P1EventScore:
        P2Points=P2Points+1
        print(P2.GetName(),"you win this event")
    else:
        print("The event is a draw")
if P1Points>P2Points:
    print(P1.GetName(),"You have won",P1Points,"Points")
elif P2Points>P1Points:
    print(P2.GetName(),"You have won this",P1Points,"Points")
else:
    print("It's a draw")

