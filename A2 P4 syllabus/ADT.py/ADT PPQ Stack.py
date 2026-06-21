#ADT ALL STACK QUESTIONS
#Question 4a
#Stack
#DECLARE stackdata [0:9] OF INTEGER
#b
stackdata=[0]*10
stackpointer=0
def pro():
    for x in range(len(stackdata)):
        print(stackdata[x])
    print(stackpointer)
#c
def Push(value):
    global stackdata
    global stackpointer
    if stackpointer>9:
        return False
    else:
        stackdata[stackpointer]=value
        stackpointer=stackpointer+1
        return True
#d
for i in range(11):
    userinp=input("Enter 10 Numbers:")
    if Push(userinp)==True:
        print("Successfully added")
    else:
        print("Not Successful")
print(stackdata)
#Question 7a
#Stack
#DECLARE Animal:ARRAY [0:19] OF STRING
#DECLARE Colour:ARRAY [0:9] OF STRING
Animal=[""]*20
AnimalTopPointer=0
Colour=[""]*10
ColourTopPointer=0
#b
def PushAnimal(DataToPush):
    global Animal
    global AnimalTopPointer
    if AnimalTopPointer==20:
        return False
    else:
        Animal[AnimalTopPointer]=DataToPush
        AnimalTopPointer=AnimalTopPointer+1
        return True
#c
def PopAnimal():
    global Animal
    global AnimalTopPointer
    if AnimalTopPointer==0:
        return ""
    else:
        AnimalTopPointer=AnimalTopPointer-1
        ReturnData=Animal[AnimalTopPointer]
        return ReturnData
#d
def ReadData():
    try:
        File=open("AnimalData.txt","r")
        for line in File:
            PushAnimal(line.strip())
        File.close()
    except IOError:
        print("File Doesn't Exists or Incorrect File Name")
#f
def PushColour(Item):
    global ColourTopPointer
    global Colour
    if ColourTopPointer==10:
        return False
    else:
        Colour[ColourTopPointer]=Item
        ColourTopPointer=ColourTopPointer+1
        return True
def PopColour():
    global Colour
    global ColourTopPointer
    if ColourTopPointer==0:
        return ""
    else:
        ColourTopPointer=ColourTopPointer-1
        ReturnData=Colour[ColourTopPointer]
        return ReturnData
#g
def ReadData():
    try:
        File=open("ColourData.txt","r")
        for line in File:
            PushColour(line.strip())
        File.close()
    except IOError:
        print("File Doesn't Exists or Incorrect File Name")
#h
def OutputItems():
    temp1=PopColour()
    temp2=PopAnimal()
    if temp1=="":
        PushAnimal(temp2)
        print("No Colour")
    elif temp2=="":
        PushColour(temp1)
        print("No Animal")
    else:
        print(temp1+" "+temp2)
#i
ReadData()
for i in range(4):
    OutputItems()
#Question 10a 27
#Stack
#DECLARE StackVowel:ARRAY [0:99] OF STRING
#DECLARE StackConsonants:ARRAY [0:99] OF STRING
StackVowel=[""]*100
StackConsonants=[""]*100
#b
#DECLARE VowelTop :INTEGER
#DECLARE ConsonantsTop :INTEGER
VowelTop=0
ConsonantsTop=0
#c
def PushData(letter):
    global VowelTop
    global ConsonantsTop
    global StackVowel
    global StackConsonants
    if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
        if VowelTop==100:
            print("Stack is Full")
        else:
            StackVowel[VowelTop]=letter
            VowelTop=VowelTop+1
    else:
        if ConsonantsTop==100:
            print("Stack is Full")
        else:
            StackConsonants[ConsonantsTop]=letter
            ConsonantsTop=ConsonantsTop+1
#d
def ReadData():
    try:
        file=open("StackData.txt","r")
        for line in file:
            PushData(line.strip())
        file.close()
    except IOError:
        print("File Not Found")
#e
def PopVowel():
    global VowelTop
    global ConsonantsTop
    global StackVowel
    if VowelTop==0:
        return "No Data"
    else:
        value=StackVowel[VowelTop]
        VowelTop=VowelTop-1
        return value
def PopConsonants():
    global VowelTop
    global ConsonantsTop
    global StackConsonants
    if ConsonantsTop==0:
        return "No Data"
    else:
        Value=StackConsonants[ConsonantsTop]
        ConsonantsTop=ConsonantsTop+1
        return Value
#f
ReadData()
VowelTop=0
ConsonantsTop=0
Letters=""
Flag=False
for x in range(5):
    Flag=False
    while Flag==False:
        choice=input("Vowel or Consonatns").lower()
        if choice=="vowel":
            DataAccessed=PopVowel()
            if DataAccessed=="No Data":
                Letters=Letters+DataAccessed
                Flag=True
            else:
                print("No vowels Left")
        elif choice=="consonants":
            DataAccessed=PopConsonants()
            if DataAccessed=="No Data":
                Letters=Letters+DataAccessed
                Flag=True
            else:
                print("No Consonants Left")
print(Letters)
#g












        
         
    

        

    

    
    
    
    