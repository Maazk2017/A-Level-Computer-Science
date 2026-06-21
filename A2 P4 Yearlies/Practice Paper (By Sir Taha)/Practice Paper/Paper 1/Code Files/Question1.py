# DECLARE nameData : ARRAY [0 : 6] OF STRING
nameData = ["Farjad", "Khadija", "Ali", "Mazin", "Taha", "Fakhir", "Zainab"]

def linearSearch( name ):
    #Declare x : INTEGER
    for x in range(0, 7):
        if nameData[x] == name:
            return True
    return False

# DECLARE username : STRING
# DECLARE temp : BOOLEAN
username = input("Enter the name: ")

temp = linearSearch(username)

if temp == True:
    print("The Name was found")
else:
    print("The name was not found")

def insertionSort():
    #DECLARE pointer, holePosition : INTEGER
    #DECLARE valuetoinsert : STRING
    for pointer in range(1, 7):
        valuetoinsert = nameData[pointer]
        holePosition = pointer

        while holePosition > 0 and nameData[holePosition -1] > valuetoinsert:
            nameData[holePosition] = nameData[holePosition - 1 ]
            holePosition = holePosition - 1

        nameData[holePosition] = valuetoinsert

insertionSort()
print(nameData)
