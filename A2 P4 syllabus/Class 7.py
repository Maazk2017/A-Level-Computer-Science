
#2D ARRAY
Array2D=[[0,0.0,0],[0,0,0,0],[0,0,0,0,0,0]]
# 5 rows 4 col
#ROWS= small square brackets 
#COL= values in small array
#PRACTICE QUESTION 
array_2d=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,"FAISAL",0,0,0,0]]
# 3 rows 6 col
Array2D[2][4]=43
for x in range(len(Array2D)):
    print(Array2D[x])
#Index starts from 1 
#Row & Col starts from 0
flag=True
for row in range(3):
    for col in range(6):
        if array_2d[row][col]!="FAISAL":
            falg=False
if flag==True:
    print("Not Found")
else:
    print("Present")






