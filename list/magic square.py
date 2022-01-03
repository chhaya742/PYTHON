square=[[8, 3, 4],
   [1, 5, 9],
   [6, 7, 2]]
rows=0
colomn=0
d=0
d2=0
for i in range(0,len(square)):
    j=2
    for j in range(0,len(square)):
        rows+=square[i][j]
        colomn+=square[j][i]
    d+=square[i][i]
    d2+=square[i][j]
    j-=1
if rows==colomn and d==d2:
    print("ist magic square")
else:
    print("not a magic square")
        

