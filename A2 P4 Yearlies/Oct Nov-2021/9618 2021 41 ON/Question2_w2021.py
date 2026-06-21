class Picture():
    # PRIVATE Description: STRING
    # PRIVATE Width: INTEGER
    # PRIVATE Height: INTEGER
    # PRIVATE FrameColour: STRING
    def __init__(self, Description, Width, Height, FrameColour):
        self.__Description = Description
        self.__Width = Width
        self.__Height = Height
        self.__FrameColour = FrameColour

    # Part b
    def GetDescription(self):
        return self.__Description

    def GetHeight(self):
        return self.__Height  # Fixed by adding the return statement

    def GetWidth(self):
        return self.__Width

    def GetColour(self):
        return self.__FrameColour

    # Part c
    def SetDescription(self, newdescription):
        self.__Description = newdescription


# Part d
# DECLARE PictureArray: ARRAY[0:99] OF Picture
PictureArray = []


# Part e
def ReadNodeData():
    try:
        File = open("Pictures.txt", "r")
        for x in range(21):  # Adjust this number based on how many pictures you have
            Descriptionline = File.readline().strip()
            Widthline = int(File.readline().strip())
            Heightline = int(File.readline().strip())
            Colourline = File.readline().strip()
            PictureObject = Picture(Descriptionline, Widthline, Heightline, Colourline)
            PictureArray.append(PictureObject)
        File.close()
    except IOError:
        print("File does not exist")


# Part f
ReadNodeData()

# Debugging: Print the loaded PictureArray to ensure NodeData is loaded correctly
print("Loaded Pictures:")
for picture in PictureArray:
    print(f"Description: {picture.GetDescription()}, Width: {picture.GetWidth()}, Height: {picture.GetHeight()}, Colour: {picture.GetColour()}")

# Part g
Found = False
userdes = input("Enter the description:").strip().lower()  # Convert to lowercase and strip extra spaces
userwid = int(input("Enter the width:"))
userhei = int(input("Enter the Height:"))
usercol = input("Enter the colour:").strip().lower()  # Convert to lowercase and strip extra spaces

# Debugging: Print out the user input
print("\nUser input:")
print(f"Description: {userdes}, Width: {userwid}, Height: {userhei}, Colour: {usercol}")

# Search for a matching picture
for x in range(len(PictureArray)):
    picture = PictureArray[x]
    
    # Debugging: Print out the details being compared
    print(f"\nComparing with picture {x + 1}")
    print(f"Picture Description: {picture.GetDescription().lower()}, Width: {picture.GetWidth()}, Height: {picture.GetHeight()}, Colour: {picture.GetColour().lower()}")
    
    if (userdes == picture.GetDescription().strip().lower() and
        userwid == picture.GetWidth() and
        userhei == picture.GetHeight() and
        usercol == picture.GetColour().strip().lower()):
        
        print(f"\nMatch found for picture {x + 1}!")
        print(picture.GetDescription())
        print(picture.GetWidth())
        print(picture.GetHeight())
        print(picture.GetColour())
        Found = True
        break

if not Found:
    print("No matching pic found")


