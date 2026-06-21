
LinkedList=[(1,1),(5,4),(6,7),(7,-1),(2,2),(0,6),(0,8),(56,3),(0,9),(0,1)]
startpointer=0
emptylist=5
def addnode(currentpointer):
    global LinkedList
    global startpointer
    global emptylist
    data=int(input("Enter The Data That You Want To Add: "))
    if emptylist<0 and emptylist>9:
        return False
    else:
        freelist=emptylist
        emptylist=LinkedList[emptylist][1]
        LinkedList[freelist]=[data][-1]
        while currentpointer!=-1:
            previouspointer=currentpointer
            currentpointer=LinkedList[currentpointer][1]
        LinkedList[previouspointer][1]=emptylist
        return True
addnode(startpointer)
#
def deletenode():
    global LinkedList
    global startPointer
    global emptyList
    currentpointer=startPointer
    Data=int(input("Enter The Data You Are Trying To Remove"))
    while currentpointer!=-1 and LinkedList[currentpointer][0]!=Data:
        previouspointer=currentpointer
        currentpointer=LinkedList[currentpointer][1]
    if currentpointer==-1:
        return False
    else:
        if currentpointer==startpointer:
            startpointer=LinkedList[startpointer][1]
        else:
            LinkedList[previouspointer][1]=LinkedList[currentpointer][1]
        LinkedList[currentpointer][0]=0
        LinkedList[currentpointer][1]=emptylist
        emptylist=currentpointer
        return True
#
def orderedInsertion(currentpointer):
    global LinkedList
    global emptyList
    global startPointer
    #Step1:Input the value you want to insert
    datatoinsert=int(input("Enter the data you want to add: "))
    if emptylist<0 and emptylist>9:
        return False
    else:
        freelist=emptylist
        emptylist=LinkedList[emptylist][1]
        LinkedList[freelist]=[datatoinsert][-1]
        while currentpointer!=-1 and datatoinsert>LinkedList[currentpointer][0]:
            previouspointer=currentpointer
            currentpointer=LinkedList[currentpointer][1]
        if currentpointer==startpointer:
            LinkedList[freelist][1]=startpointer
            startpointer=freelist
        else:
            LinkedList[freelist][1]=LinkedList[previouspointer][1]
            LinkedList[previouspointer]=freelist
            return True

    






