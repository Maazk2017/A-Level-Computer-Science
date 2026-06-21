#Practice Question
#Print the complete file by using readfile
file=open("HighScore.txt","r")
for x in range(20):
    temp=file.readline()
    print(temp)
file.close()
#New Line Character
#print fuctin already has a new line funtion
print("Taha\n\n")
print("Bano\n")
print("Pappan")
#so how to give gap in files
File=open("Students.txt","w")
File.write("Griffith\n")
File.write("Guts\n")
#output will be shown in the students file .txt
#or how to do the same thing in previous question
#we use the strip() method
file=open("HighScore.txt","r")
for x in range(20):
    print(file.readline().strip())
file.close()
#Practice Question
#find the sum of all players
sum=0
file=open("HighScore.txt","r")
for x in range(10):
    player=file.readline().strip()
    score=file.readline().strip()
    sum=sum+int(score)
print(sum)
file.close
x=1
sum=0
file=open("HighScore.txt","r")
#with while loop
file=open("HighScore.txt","r")
while x<21:
    player1=file.readline().strip()
    score1=file.readline().strip()
    sum=sum+int(score1)
    x=x+2
print(sum)
file.close
#Practice Question
#create an array with 10 elements in which you store all the player names and scores from file highscore.txt
#Declare file data:Array[0:9,0:1] OF STRING
filedata=[[""]*2 for i in range(10)]
file=open("HighScore.txt","r")
for row in range(10):
    filedata[row][0]=file.readline().strip()
    filedata[row][1]=file.readline().strip()
print(filedata)
file.close
#part c
def OutputHighScores():
    for row in range(10):
        line=filedata[row][0]+" "+filedata[row][1]
        print(line)
OutputHighScores()
File=open("Newkt.txt","w")
File.write("pv=nkt\n")
File.write("fgrjh\n")


    





