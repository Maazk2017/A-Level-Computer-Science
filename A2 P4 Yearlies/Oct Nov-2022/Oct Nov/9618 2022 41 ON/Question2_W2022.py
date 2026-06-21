#Part ai
class Card():
    #PRIVATE Number:INTEGER
    #PRIVATE Colour:STRING
    def __init__(self,Number,Colour):
        self.__Number=Number
        self.__Colour=Colour
#Part aii
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour
#Part aiii
Red1=Card(1,"red")
Red2=Card(2,"red")
Red3=Card(3,"red")
Red4=Card(4,"red")
Red5=Card(5,"red")

Blue1=Card(1,"blue")
Blue2=Card(2,"blue")
Blue3=Card(3,"blue")
Blue4=Card(4,"blue")
Blue5=Card(5,'blue')

Yellow1=Card(1,"yellow")
Yellow2=Card(2,"yellow")
Yellow3=Card(3,"yellow")
Yellow4=Card(4,"yellow")
Yellow5=Card(5,"yellow")

#Part bi
class Hand():
    #PRIVATE Cards:ARRAY[0:9]OF Card
    #PRIVATE FirstCard:INTEGER
    #PRIVATE NumberOfCards:INTEGER
    def __init__(self,Card1,Card2,Card3,Card4,Card5):
        self.__Cards=[]
        self.__Cards.append(Card1)
        self.__Cards.append(Card2)
        self.__Cards.append(Card3)
        self.__Cards.append(Card4)
        self.__Cards.append(Card5)
        self.__FirstCard=0
        self.__NumberOfCards=5
#Part bii
    def GetCard(self,index):
        return self.__Cards[index]
#Part biii
Player1=Hand(Red1,Red2,Red3,Red4,Yellow1)
Player2=Hand(Yellow2,Yellow3,Yellow4,Yellow5,Blue1)
#Part ci
def CalculateValue(Player):
    Points=0
    for x in range(5):
        PlayerObject=Player.GetCard(x)
        HandNumber=PlayerObject.GetNumber()
        HandColour=PlayerObject.GetColour()
        if HandColour=="red":
            Points=Points+5
        elif HandColour=="yellow":
            Points=Points+15
        else:
            Points=Points+10
        Points=Points+HandNumber
    return Points
#Part cii
Temp1=CalculateValue(Player1)
Temp2=CalculateValue(Player2)
if Temp1>Temp2:
    print("Player1 wins")
elif Temp2>Temp1:
    print("Player2 wins")
else:
    print("Draw")
#Part ciii






    


        
