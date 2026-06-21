#PRACTICE QUESTION (OBJECT ORIENTED PROGRAMMING)
#Q1 
class Picture():
    #PRIVATE Description :STRING
    #PRIVATE Width:INTEGER
    #PRIVATE Height:INTEGER
    #PRIVATE FrameColour:STRING
    def __init__(self,PicDescripton,PicWidth,PicHeight,PicFrame):
        self.__Description=PicDescripton
        self.__Width=PicWidth
        self.__Height=PicHeight
        self.__FrameColour=PicFrame
    def GetDescription(self):
        return self.__Description
    def GetHeight(self):
        return self.__Height
    def GetWidth(self):
        return self.__Width
    def GetColour(self):
        return self.__FrameColour
    def setDescription(self,newdescription): #*
        self.__Description=newdescription

        
#Instance of the class(object creation)
MyPicture=Picture("Mona Lisa",200,400,"Black")
temp=MyPicture.GetDescription
print(temp)

response=input("Do you want to change discription:(Y/N)")
if response=="Y":
    MyPicture.setDescription("Shabnam ki prem kahani")
temp_2=MyPicture.GetDescription()
print(temp_2)



class Picture():
    def __init__(self,Descriptionp,widthp,heightp,framecolourp):
        self.__Description=Descriptionp
        self.__width=widthp
        self.__height=heightp
        self.__framecolour=framecolourp
    def GetDescription(self):
        return self.__Description
    def GetHieght(self):
        return self.__height
    def GetWidth(self):
        return self.__width
    def GetColour(self):
        return self.__framecolour
    def SetDescription(self,newdes):
         self.__Description=newdes
    def SetColour(self,newcol):
         self.__framecolour=newcol
Pic=Picture("The Moment",2000,1500,"White")
temp=Pic.GetDescription()
print(temp)
Pic.SetDescription("Memento")
temp1=Pic.GetDescription()
print(temp1)



