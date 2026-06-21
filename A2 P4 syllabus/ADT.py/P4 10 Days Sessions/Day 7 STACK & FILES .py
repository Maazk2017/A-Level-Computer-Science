#DECLARE Animal:ARRAY[0:9] OF STRING
#DECLARE Colour:ARRAY[0:9] OF STRING
#DECLARE AnimalTopPointer:INTEGER
#DECLARE ColourTopPointer:INTEGER
#Part a
global Animal
global Colour
Animal=[""]*20
AnimalTopPointer=0
Colour=[""]*10
ColourTopPointer=0
#Part b
def PushAnimal(DataToPush):
    global Animal
    global AnimalTopPointer
    if AnimalTopPointer==20:
        return True
    else:
        Animal[AnimalTopPointer]=DataToPush
        AnimalTopPointer=AnimalTopPointer+1
        return True
#Part c
def PopAnimal():
    global Animal 
    global AnimalTopPointer
    if AnimalTopPointer==0:
        return ""
    else:
        ReturnData=Animal[AnimalTopPointer-1]
        AnimalTopPointer=AnimalTopPointer-1
        return ReturnData
#Part d
def ReadData():
    global Animal
    global AnimalTopPointer
    try:
        File=open("AnimalData.txt","r")
        for line in File:
            PushAnimal(line.strip())
        File.close()
    except IOError:
        print("File Doesn't Exists")
#Part e
def PushColour(Item):
    global Colour
    global ColourTopPointer
    if ColourTopPointer==20:
        return False
    else:
        Colour[ColourTopPointer]=Item
        ColourTopPointer=ColourTopPointer
        return True
def PopColour():
    global Colour
    global ColourTopPointer
    if ColourTopPointer==0:
        return ""
    else:
        ReturnItem=Colour[ColourTopPointer-1]
        ColourTopPointer=ColourTopPointer-1
        return ReturnItem
#Part f
def ReadData():
    global Colour
    global ColourTopPointer
    try:
        File=open("ColourData.txt","r")
        for line in File:
            PushColour(line.strip())
        File.close()
    except IOError:
        print("File Doesn't Exists")
#Part g
def OutputItems():
    temp1=PopAnimal()
    temp2=PopColour()
    if temp2=="":
        PushAnimal(temp1)
        print("No Colour")
    elif temp1=="":
        PushColour(temp2)
        print("No Animal")
    else:
        print(temp2+" "+temp1)
#Part h
ReadData()
OutputItems()
OutputItems()
OutputItems()
OutputItems()

        
    
        


