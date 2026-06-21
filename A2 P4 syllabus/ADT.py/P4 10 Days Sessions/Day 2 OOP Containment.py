class Card():
#Part a
    #PRIVATE Number:INTEGER
    #PRIVATE Colour:STRING
    def __init__(self,Number,Colour):
        self.__Number=Number
        self.__Colour=Colour
#Part b
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour
#Part c
Red1=Card(1,"red")
Red2=Card(2,"red")
Red3=Card(3,"red")
Red4=Card(4,"red")
Red5=Card(5,"red")

Blue1=Card(1,"blue")
Blue2=Card(2,"blue")
Blue3=Card(3,"blue")
Blue4=Card(4,"blue")
Blue5=Card(5,"blue")

Yellow1=Card(1,"yellow")
Yellow2=Card(2,"yellow")
Yellow3=Card(3,"yellow")
Yellow4=Card(4,"yellow")
Yellow5=Card(5,"yellow")

#Part d
class Hand():
    #PRIVATE FirstCard:INTEGER
    #PRIVATE NumberCard:INTEGER
    #PRIVATE Cards:ARRAY[0:9] OF Card
    def __init__(self,Card1,Card2,Card3,Card4,Card5):
        self.__Card=[0]*10
        self.__Card[0]=Card1
        self.__Card[1]=Card2
        self.__Card[2]=Card3
        self.__Card[3]=Card4
        self.__Card[4]=Card5
        self.__FirstCard=0
        self.__NumberCards=5
#Part e
    def GetCard(self,Index):
        return self.__Card[Index]
#Part f
Player1=Hand(Red1,Red2,Red3,Red4,Yellow1)
Player2=Hand(Yellow2,Yellow3,Yellow4,Yellow5,Blue1)
#Part g
def CalCulateValue(HandObject):
    score=0
    for index in range(5):
        HandCard=HandObject.GetCard(index)
        colour=HandCard.GetColour()
        number=HandCard.GetNumber()
        if colour=="red":
            score=score+5
        elif colour=="yellow":
            score=score+10
        else:
            score=score+15
        score=score+number
    return score
#Part h
temp1=CalCulateValue(Player1)
temp2=CalCulateValue(Player2)
if temp1>temp2:
    print("Player1 Wins")
elif temp2>temp1:
    print("Player2 Wins")
else:
    print("Draw")

    
        
