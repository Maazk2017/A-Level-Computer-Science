Myfile=open("HighScore.txt","r")
text=Myfile.read()
print(text)
Myfile.close()
#Read.line Function
file=open("HighScore.txt","r")
firstline=file.readline()
secondline=file.readline()
print(firstline)
print(secondline)


myfile=open("HighScore.txt","r")
print(myfile.read())

