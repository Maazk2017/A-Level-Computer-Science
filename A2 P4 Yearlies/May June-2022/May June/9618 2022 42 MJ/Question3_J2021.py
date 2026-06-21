#Part a 
class Card():
    #PRIVATE Number:INTEGER
    #PRIVATE Colour:STRING
    def __init__(self,Number,Colour):
        self.__Number=Number
        self.__Colour=Colour
#Part b
    def GetNumber(self):
        self.__Number
    def GetColour(self):
        self.__Colour
#Part c
#DECLARE CardArray:ARRAY[0:29] OF Card
CardArray=[0]*30
File=open("CardValues.txt","r")
for x in range(30):
    CardNumber=int(File.readline().strip())
    CardColour=File.readline().strip()
    CardArray=Card(CardNumber,CardColour)
File.close()
#Part d
NumbersChosen=[False]*30
def ChooseCard():
    global NumbersChosen
    Flag=False
    while Flag==False:
        userinp=int(input("Enter a number b/w 1 & 30:"))
        if userinp<1 or userinp>30:
            print("Number not in range")
        elif NumbersChosen[userinp-1]==True:
            print("alreadt taken")
        else:
            print("Valid")
            Flag=True
    NumbersChosen[userinp-1]=True
    return userinp-1
#Part ei
#DECLARE Player1:ARRAY[0:3] OF Card
Player1=[]
for x in range(3):
    Temp=ChooseCard()
    Player1.append(CardArray[Temp])
for x in range(3):
    print(Player1[x].GetNumber())
    print(Player1[x].GetColour())
#Part eii

            

        


        
