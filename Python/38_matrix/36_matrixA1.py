#matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
print(matrix[0])
print(matrix[0][0])

matr = []
col = 4 #oszlop
row = 4 #sor

#Matrix létrehozása
for r in range(row):
    lista = []
    for c in range(col):
        lista.append(0)
    matr.append(lista)
#Végighaladás rajta
for r in range(row):
    for c in range(col):
        print(matr[r][c], end=" ")
    print()


print()
matr = []
col = 5 #oszlop
row = 5 #sor

#Matrix létrehozása
for r in range(row):
    lista = []
    for c in range(col):
        
        if r == c:
            lista.append("x")
        else:
            lista.append(0)
    matr.append(lista)
#Végighaladás rajta
for r in range(row):
    for c in range(col):
        print(matr[r][c], end=" ")
    print()

