#Global & Local Variable
#GLobal :Shared mail box
#Local :Specific hotel room
#GLOBAL SCOPE :Values which exists outside the fuction
#LOCAL SCOPE :Values which exist inside the fuction



number=6 #Global Scope
def check():
    #Local Scope
    number=5
    print("Ye kamre ke ander hai",number)
check()
print("ye shared apartment wala hai",number)


#BY VAL BY REF
YourResult="3A" #Global ORIGNAL DOCUMENT
#apke orignal result ki copy banjeygi
# now i want to make change to your actual result
def ChangeResult():
    global YourResult#Passing the parameter by refrence
    if YourResult=="3A":
        YourResult="3A*"
    print("Kamre ke andar your result",YourResult)
ChangeResult() #BY VALUE
#apke orignal result ki copy banjeygi
#or ham us ko pass kardenge 
#so change in copy wont make changes in your resutl
#bole to global me koi change nahi ho rha 
print("Kamre ke bahir",YourResult)







