print("Kérek egy számot és felsorolom a szám osztóit!")
print("Kilépéshez írd be, hogy \"quit\"!")


#szintaktikai, szemantikai hibák
def osztoi(x):
    osztok = []
    for i in range(1, x):       #x+1
        if x % i = 0:           #==
            osztok.apend(i)     #append
    return osztok

while True:
    number = input("Adj meg egy számot: ")
    osztok_lista = []
    if number == "quit":    
        print("Kiléptél a programból!")
        break
    elif not number.isnumeric():
        print("Hibás értéket vagy parancsot adtál meg!\nSzámokat írj be, vagy ha esetleg kilépni akartál:\n\tquit")
    else:
        print(f"A(z) {number} osztói: ", end="")
        osztok_lista = osztoi()     #int(number)
        text = ""
        for x in osztok_lista:
            if osztok_lista.index(x) != len(osztok_lista)-1:
                text = text + str(x) + "; "
            else:
                text = text + str(x)
        print(text)

            
        