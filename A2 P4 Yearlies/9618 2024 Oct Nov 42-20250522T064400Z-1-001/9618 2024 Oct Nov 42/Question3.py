#Part a
#DECLARE HighScore:ARRAY[0:2,0:6] OF STRING
HighScores=[[""]*3 for i in range(7)]
#Part b
def ReadData():
    try:
        File=open("HighScoreTable.txt","r")
        for x in range(7):
            ID=File.readline().strip()
            GameLevel=int(File.readline().strip())
            Score=int(File.readline().strip())
            HighScores[x][0]=ID              #Remember row comes first the columns in assingnmets
            HighScores[x][1]=GameLevel
            HighScores[x][2]=Score
        File.close()
    except IOError:
        print("File Doesn't Exists")
    return HighScores
#Part c
def OutputHighScores(NewArray):
    for x in range(7):
        ID=NewArray[x][0]
        GameLevel=NewArray[x][1]
        Score=NewArray[x][2]
        print(ID,"Reached level",GameLevel,"with a score of",Score)
#Part d
def SortScores(HighScores1):
    Boundary=6
    noswap=False
    while noswap==False:
        noswap=True
        for y in range(Boundary):
            if int(HighScores1[y][1])>int(HighScores1[y+1][1]):
                Temp=HighScores1[y]
                HighScores1[y]=HighScores1[y+1]
                HighScores1[y+1]=Temp
            elif int(HighScores1[y][1])==(HighScores1[y][1]) and int(HighScores1[y][2])<int(HighScores1[y+1][2]):
                Temp=HighScores1[y]
                HighScores1[y]=HighScores1[y+1]
                HighScores1[y+1]=Temp
        Boundary=Boundary-1
    return HighScores1
#Part ei
Temp=ReadData()
print("Before")
OutputHighScores(Temp)
SortScores(HighScores)
print("After")
OutputHighScores(HighScores)

