lista1 = [2, 4, 5, 9, 12, 3, 9, 4]

def minimum(lista):
    minElem = lista[0]
    for elem in lista:
        if elem < minElem:
            minElem = elem
    return minElem

print(minimum(lista1))


def maximum(lista):
    maxElem = lista[0]
    for elem in lista:
        if elem > maxElem:
            maxElem = elem
    return maxElem

print(maximum(lista1))

ker = 5
def eldontes(lista, k):
    n = len(lista)
    i = 0
    while i < n and lista[i] != k:
        i = i + 1
    if i < n:
        print("Meg van a", k)
    else:
        print("Nincs meg a", k)

