#Part a
global DataStored
global NumberWords
WordArray=[]
NumberWords=0
def ReadWords(FileName):
    global DataStored
    global NumberWords
    try:
        File=open(FileName,"r")
        for line in File:
            WordArray.append(line.strip())
            NumberWords=NumberWords+1
        NumberWords=NumberWords-1
        File.close()
    except IOError:
        print("Fiel Doesn't Exists")

#Part b
userinp=input("Enter east,medium or hard:")
if userinp.lower()=="easy":
    FileName="Easy.txt"
elif userinp.lower()=="medium":
    FileName="Medium.txt"
else:
    FileName="Hard.txt"
ReadWords(FileName)          
#Part ci
#Part cii
def Play():
    global NumberWords
    global WordArray
    print(WordArray[0],"The main word")
    print(NumberWords,"Number of Answers")
    Count=0
    Flag=False
    while Flag==False:
        userinp=input("Enter Word:")
        if userinp.lower()=="no":
            Flag=True
        else:
            AnswerFlag=False
            for x in range(1,NumberWords+1):
                if WordArray[x]==userinp.lower():
                    print(" Yes it is an answer")
                    Count=Count+1
                    WordArray[x]=""
                    AnswerFlag=True
            if AnswerFlag==False:
                print("It is not the answer")
    percentage=int((Count/NumberWords)*100)
    print(percentage)
    for x in range(1,NumberWords+1):
        if WordArray[x]!=userinp.lower():
            print(WordArray[x])
#Part di
def ReadWords(FileName):
    global DataStored
    global NumberWords
    try:
        File=open(FileName,"r")
        for line in File:
            WordArray.append(line.strip())
            NumberWords=NumberWords+1
        NumberWords=NumberWords-1
        File.close()
    except IOError:
        print("File Doesn't Exists")
#Part di
    Play()
ReadWords(FileName)          






        





    



    

