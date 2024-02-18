


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
print(matrix[0])
print(matrix[0][0])
           #s   o


row = 4     #sor
col = 4     #oszlop

#Matrix létrehozása - feltöltése
matr = []
for r in range(row):
    list = []
    for c in range(col):
        list.append(0)
    matr.append(list)
#Matrix bejárása
for r in range(row):
    for c in range(col):
        print(matr[r][c], end=" ")
    print()
