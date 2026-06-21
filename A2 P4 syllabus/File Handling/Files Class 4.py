#If you are not aware of number of lines
file=open("HighScore.txt","r")
for line in file:                         # we will use variable name instead pf range
    print(line.strip())
file.close()
#Another Method
File=open("HighScore.txt","r")
Flag=True
# if the end of file is reached readline returns empty an string ""
while Flag==True:
    temp=File.readline().strip()
    if temp=="":
        Flag=False
    else:
        print(temp)
File.close()    
#Practice Question
File=open("EventGuest.txt","r")
Flag=False
for line in File:
    if line.strip()=="Paperdock":
        print("Already Invited")
        Flag=True
File.close()
File=open("EventGuest.txt","a")
if Flag==False:
    File.write("Papersdock\n")
File.close()
    


