#Part ai
class Horse():
    #PRIVATE Name:STRING
    #PRIVATE MaxFenceHeight:INTEGER
    #PRIVATE PercentageSuccess:INTEGER
    def __init__(self,Name,MaxFenceHeight,PercentageSuccess):
        self.__Name=Name
        self.__MaxFenceHeight=MaxFenceHeight
        self.__PercentageSuccess=PercentageSuccess
#Part ii
    def GetName(self):
        return self.__Name
    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight
#Part d
    def Success(self,Height,Risk):
        if Height>self.__MaxFenceHeight:
            return self.__PercentageSuccess*0.2
        else:
            if Risk==1:
                return self.__PercentageSuccess*1
            elif Risk==2:
                return self.__PercentageSuccess*0.9
            elif Risk==3:
                return self.__PercentageSuccess*0.8
            elif Risk==4:
                return self.__PercentageSuccess*0.7
            else:
                return self.__PercentageSuccess*0.6 
#Part bi
#DECLARE Horses:ARRAY [0:2] OF Horse
Horses=[]
Horses.append(Horse("Beauty",150,72))
Horses.append(Horse("Jet",160,65))
print(Horses[0].GetName())
print(Horses[1].GetName())
#Part bii
#Screenshot
#Part ci
class Fence():
    #PRIVATE Height:INTEGER
    #PRIVATE Risk:INTEGER
    def __init__(self,Height,Risk):
        self.__Height=Height
        self.__Risk=Risk
    def GetHeight(self):
        return self.__Height
    def GetRisk(self):
        return self.__Risk
#Part cii
#DECLARE Course:ARRAY[0:4] OF Fence
Course=[]
for x in range(4):
    HeightFlag=False
    while HeightFlag==False:
        height=int(input("Enter the valid height:"))
        if height>=70 and height<=180:
            HeightFlag=True
    RiskFlag=False
    while RiskFlag==False:
        risk=int(input("Enter valid risk:"))
        if risk>=1 and risk<=5:
            RiskFlag=True
    FenceObj=Fence(height,risk)
    Course.append(FenceObj)    
#Part ei
AverageSuccess=[]
for y in range(2):
    Total=0
    for x in range(4):
        height=Course[x].GetHeight()
        Risk=Course[x].GetRisk()
        chance=Horses[y].Success(height,Risk)
        Total=Total+chance
        print(Horses[y].GetName(),"Fence",x+1,"Chance of success is ",chance)
    Avg=int((Total/4))
    AverageSuccess.append(Avg)
    print(Horses[y].GetName(),"average success rate is",Avg,"%")
if AverageSuccess[0]>AverageSuccess[1]:
    name=Horses[0].GetName()
else:
    name=Horses[1].GetName()
print(name,"has better chance")



