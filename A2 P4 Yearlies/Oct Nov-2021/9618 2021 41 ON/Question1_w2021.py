#Part a
def Unkown(X,Y):
    if X<Y:
        return (Unkown(X+1,Y)*2)
    elif X==Y:
        return 1
    else:
        print(X+Y)
        return (Unkown(X-1,Y)//2)
#Part bi
return1=Unkown(10,15)
print("x is",10)
print("y is",15)
print(return1)
return2=Unkown(10,10)
print("x is",10)
print("y is",10)
print(return2)
return3=Unkown(15,10)
print("x is",15)
print("y is",10)
print(return3)
#Part bii
#Part c
def IterativeUnkown(X,Y):
    Total=1
    while X!=Y:
        if X<Y:
            print(X+Y)
            X=X+1
            Total=Total*2
        else:
            print(X+Y)
            X=X-1
            Total=Total//2
    return Total
#Part di
return1=IterativeUnkown(10,15)
print("x is",10)
print("y is",15)
print(return1)
return2=IterativeUnkown(10,10)
print("x is",10)
print("y is",10)
print(return2)
return3=IterativeUnkown(15,10)
print("x is",15)
print("y is",10)
print(return3)
#Part dii


    

        





        
    