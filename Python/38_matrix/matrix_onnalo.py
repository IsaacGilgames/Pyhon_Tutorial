"""
row = 5     
col = 5     
matr = []
for r in range(row):
    list = []
    for c in range(col):
        if c == r:
            list.append("x")
        else:
            list.append(0)
    matr.append(list)

for r in range(row):
    for c in range(col):
        print(matr[r][c], end=" ")
    print()
"""

row = 5     
col = 5     
matr = []
i = row-1
for r in range(row):
    list = []
    for c in range(col):
        if c == i:
            list.append("x")
        else:
            list.append(0)
    i -=1
    matr.append(list)

for r in range(row):
    for c in range(col):
        print(matr[r][c], end=" ")
    print()


row = 5     
col = 5     
matr = []
for r in range(row, 0, -1):
    list = []
    for c in range(col):
        if r == c+1:
            list.append("x")
        else:
            list.append(0)
    matr.append(list)

for r in range(row):
    for c in range(col):
        print(matr[r][c], end=" ")
    print()