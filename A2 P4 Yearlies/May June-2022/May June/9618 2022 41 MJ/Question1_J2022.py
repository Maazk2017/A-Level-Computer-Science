
#Part a
#DECLARE FileData:ARRAY[0:10,0:1] OF STRING
FileData=[[""]*2 for i in range(11)]
#Part b
def ReadHighScores():
    try:
        File=open("HighScore.txt","r")
        for x in range(10):
            FileData[x][0]=File.readline().strip()
            FileData[x][1]=File.readline().strip()
        File.close()
    except IOError:
        print("File doen't exists")
#Part c
def OutputHighScores():
    print("PlayerName"+" "+"Score")
    for x in range(10):
        line=(str(FileData[x][0])+" "+str(FileData[x][1]))
        print(line)










        
