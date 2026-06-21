#Write Mode
file=open("NewFile.txt","w")
file.write("Maaz\n")
file.write("Taha\n")
file.close()
#Practice Question
File=open("EventGuest.txt","w")
flag=False
while flag==False:
    userinp=input("Enter The Name Of The Guest You Want To Invite: ")
    if userinp=="No":
        flag=True
    else:
        File.write(userinp +"\n")
File.close()
#Append Mode
file=open("EventGuest.txt","a")
file.write("Kalesh Puhpoo\n")
file.close()


    

    
