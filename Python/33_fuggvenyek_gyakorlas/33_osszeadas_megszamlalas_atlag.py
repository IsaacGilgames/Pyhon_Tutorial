#Fuggvenyek_gyakorlasa.py

list1 = [2, 3, 5, 1, 8, 2]
list2 = [4, 6, 4, 9, 1, 2]
list3 = [4, 2, 2, 5, 7, 8]
list4 = [5, 1, 1, 8, 7, 3]
list5 = [3, 4, 1]
list6 = [2, 5]
list7 = [5, 6, 2, 1]



def ossz(lista):
    osszeg = 0
    for x in lista:
        #osszeg = osszeg + x
        osszeg+=x
    return osszeg
    

print(f"Az első lista összege: {ossz(list1)}")

def szamol(lista):
    megszamlal = 0
    for x in lista:
        megszamlal+=1
    return megszamlal

print(f"A második lista darabszáma: {szamol(list2)}")
print(f"Az ötödik lista darabszáma: {szamol(list5)}")
print(f"A hatodik lista darabszáma: {szamol(list6)}")
print(f"A hetedik lista darabszáma: {szamol(list7)}")

def atl(lista):
    atlag = 0
    megszamol = 0
    osszeg = 0
    for x in lista:
        osszeg+=x
        megszamol+=1
    return osszeg/megszamol


def atl2(lista):
    return ossz(lista)/szamol(lista)