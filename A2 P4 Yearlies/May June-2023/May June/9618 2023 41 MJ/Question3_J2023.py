#Part a
#DECLARE Animal:ARRAY[0:20]OF STRING
#DECLARE Colour:ARRAY[0:10]OF INTEGER
#DECLARE AnimalTopPointer:INTEGER
#DECLARE ColourTopPointer:INTEGER
global Animal 
global Colour
Animal=[""]*20
Colour=[""]*10
AnimalTopPointer=0
ColourTopPointer=0
#Part bi
def PushAnimal(DataToPush):
    global Animal
    global AnimalTopPointer
    if AnimalTopPointer==20:
        return False
    else:
        Animal[AnimalTopPointer]=DataToPush
        AnimalTopPointer=AnimalTopPointer+1
        return True
#Part bii
def PopAnimal():
    global Animal
    global AnimalTopPointer
    if AnimalTopPointer==0:
        return ""
    else:
        ReturnData=Animal[AnimalTopPointer-1]
        AnimalTopPointer=AnimalTopPointer-1
        return ReturnData
#Part biii
def ReadAnimalData():
    global Animal
    try:
        File=open("AnimalData.txt","r")
        for line in File:
            PushAnimal(line.strip())
        File.close()
    except IOError:
        print("File Does'nt Exists")
#Part biv
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
        ReturnData=Colour[ColourTopPointer-1]
        ColourTopPointer=ColourTopPointer-1
        return ReturnData
#Part v
def ReadColurData():
    global Colour
    try:
        File=open("ColourData.txt","r")
        for line in File:
            PushColour(line.strip())
        File.close()
    except IOError:
        print("File Doesn't Exists or Incorrect File Name")
#Part c
def OutputItems():
    Temp1=PopAnimal()
    Temp2=PopColour()
    if Temp2=="":
        PushAnimal(Temp1)
        print("No Colour")
    elif Temp1=="":
        PushColour(Temp2)
        print("No Animal")
    else:
        line=Temp2+" "+Temp1
        print(line)    
#Part di
ReadAnimalData()
ReadColurData()
OutputItems()
OutputItems()
OutputItems()
OutputItems()
#Part dii
