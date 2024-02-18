#Írj egy Python programot, amely bekér két szót (sztringet) a felhasználótól és kiírja a képernyőre,
#hogy van-e olyan betű, amelyik mind a kettőben előfordul!

#Első megoldás
szo1 = str(input("Kérek egy szót: "))
szo2 = str(input("Kérek egy szót: "))
van = False

for betu in szo1:
    if betu in szo2:
        van = True
    
if van == True:
    print("Van olyan betű ami szerepel mind a két szóban!")
else:
    print("Nincs olyan betű ami szerepel mind a két szóban!")



#Mésodik megoldás
szo1 = str(input("Add meg az első szót: "))
szo2 = str(input("Add meg az második szót: "))

kozos_betuk = set(szo1) & set(szo2)

if kozos_betuk:
    print("Vannak közös betűk a szóban")
else:
    print("Nincsenek közös betűk a szóban")



#Harmadik megoldás
def kozos_betu(szo1, szo2):
    kozos_betu = False

    for betu in szo1:
        if betu in szo2:
            kozos_betu = True
            break  

    if kozos_betu:
        print("Van közös betű a két szóban.")
    else:
        print("Nincs közös betű a két szóban.")

szo_1 = input("Kérem az első szót: ")
szo_2 = input("Kérem a második szót: ")

kozos_betu(szo_1, szo_2)



#Negyedik megoldás
szo1 = input("Adja meg az első szót: ")
szo2 = input("Adja meg a második szót: ")

for betu in szo1:
    if betu in szo2:
        print("Van olyan betű, amely mindkét szóban előfordul.")
        break
else:
    print("Nincs olyan betű, amely mindkét szóban előfordul.")



#Ötödik megoldás
def kozos_betuk(szo1, szo2):
    betuk_szo1 = set(szo1.lower())
    betuk_szo2 = set(szo2.lower())
    
    kozos_betuk = betuk_szo1.intersection(betuk_szo2)
    
    return kozos_betuk

szo1 = input("1. szo: ")
szo2 = input("2. szo: ")
kozos = kozos_betuk(szo1, szo2)
if kozos:
    print(f"van kozos: {', '.join(kozos)}")
else:
    print("nincs kozos")



#Hatodik megoldás
x = str(input("Add meg az első szót: "))
y = str(input("Add meg az második szót: "))

kozos_betuk = set(x) & set(y)

if kozos_betuk:
    print("Vannak közös betűk a szóban")
else:
    print("Nincsenek közös betűk a szóban")

#Hetedik megoldás
szo1 = input("Adjon meg egy szót: ")
szo2 = input("Adjon meg még egy szót: ")

kozos_betuk = []
for betu in szo1:
    if betu in szo2 and betu not in kozos_betuk:
        kozos_betuk.append(betu)

if kozos_betuk:
    print(f"A következő betűk mindkét szóban előfordulnak: {kozos_betuk}")
else:
    print("Nincs olyan betű, amely mindkét szóban előfordul.")


#Nyolcadik megoldás
szo1 = str(input("Adj meg egy szót: "))
szo2 = str(input("Adj meg egy szót: "))
nincs_ugyanolyan = True
for i in range(0, len(szo1)):
    for j in range(0, len(szo2)):
        if szo1[i] == szo2[j]:
            ugyanaz = szo1[i]
            nincs_ugyanolyan = False
if nincs_ugyanolyan:
    print("Nincs olyan betű, amelyik mind a kettőben előfordul!")
else:
    print(f"A(z) {ugyanaz} betű mindkét szóban előfordul ")



#Kilencedik megoldás
a=str(input("adj meg egy szót!(1/2)").lower().replace(" ","").replace("-",""))
b=str(input("adj meg egy szót!(2/2)").lower().replace(" ","").replace("-",""))


if len(a)<len(b):
    temp=a
    a=b
    b=temp
vane=False
ottisvan=""

print("⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒")

for i in range(0, len(a),1):
    if b.count(a[i])==0:
        #print(a[i])
        #print("ellenőrzés sóhaj")
        vane=False
    else:
        #print(a[i])
        #print("HUUUUUH")
        ottisvan=a[i]
        vane=True
        break

if vane:
    print(f"hurrá! a(z) {ottisvan} betű megvan mindkettőben!!!4!")
else:
    print("nem hurrá")


#Tizedik megoldás
szo1 = input("Adj meg egy szót: ")
szo2 = input("Adj még egy szót: ")

azonos_betuk = []

for betu in szo1:
    if betu in szo2 and betu not in azonos_betuk:
        azonos_betuk.append(betu)

if len(azonos_betuk) != 0:
    print("Van olyan betű, amely mindkét szóban előfordul.")
    print(f"Az azonos betűk: {azonos_betuk}" )
else:
    print("Nincs olyan betű, amely mindkét szóban előfordul.")


#Tizenegyedik megoldás
szo1 = input("Adj meg egy szót:")
szo2 = input("Adj meg egy másik szót:")
megegyezo_betuk = []
print("Megegyező betűk:", end = " ")
for x in szo1:
    for y in szo2:
        if x == y:
            if y not in megegyezo_betuk:
                megegyezo_betuk.append(y)
for x in megegyezo_betuk:
    print(x, end="")
    if megegyezo_betuk[len(megegyezo_betuk)-1] != x:
        print(end=", ")

