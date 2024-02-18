#Készíts egy programot a következő elvárások betartásával!
#Egy tanárnak készítetek segédprogramot, aki szeretne csoportmunkát vagy párosmunkát kiadni az osztályban!
#A tanár adja meg egy osztály létszámát. Feltételezhetjük, hogy a tanár csak pozitív egész számokat fog megadni!
#A megadott adat alapján kell meghatároznotok: (2 pont)
#   1. Az osztály alkalmas-e a páros munkára? Pl:
#       a) ha igen: A(z) 22 fő létszámú osztály alkalmas a páros munkára! (4 ponnt)
#       b) ha nem: A(z) 15 fő létszámú osztály nem alkalmas a páros munkára! (3 pont)
#   2. A mai alkalommal 5 fős csoportokat alkotunk! Határozzuk
#    (3 pont)   a) ha az osztály/csoport létszáma kevesebb, mint 10; jelenjen meg: "Ez a létszám (8 fő) nem megfelelő ilyen csoportmunkás feladatra!"
#     (3 pont)  b) ha tíz, vagy több, akkor határozzuk meg a csoportok számát!
#     (6 pont)  c) öttel osztható osztálylétszám esetén írja ki pl: A(z) 20 fő osztálylétszámú osztályban 4 öt fős csapatot hozhatunk létre!
#     (6 pont)  d) öttel nem osztható osztálylétszám esetén, ha maximum 2 diáknak kéne csapatot alkotni, akkor ők száljanak be egy létező csoportba írja ki pl: A(z) 22 fő osztálylétszámú osztályban 4 csapatot hozhatunk létre, de 2 csapat hat fős lesz!
#      (5 pont) f) öttel nem osztható osztálylétszám esetén, ha miminum 3 diáknak kéne csapatot alkotni írja ki pl: A(z) 24 fő osztálylétszámú osztályban 5 csapatot hozhatunk létre, de egy csapat csak 4 fős lesz!

csoport_letszam = int(input("Adja meg a csoport létszámát?\n"))


if csoport_letszam % 2 == 0:
    print(f"A(z) {csoport_letszam} fő létszámú osztály alkalmas a páros munkára!")
else:
    print(f"A(z) {csoport_letszam} fő létszámú osztály nem alkalmas a páros munkára!")

#Első változat
if csoport_letszam < 10:
    print(f"Ez a létszám ({csoport_letszam} fő) nem megfelelő ilyen csoportmunkás feladatra!")
else:
    if csoport_letszam % 5 == 0: #ha az osztály létszáma alkalmas 5 fős csapatokra (nincs olyan csapat, amiben többen vagy kevesebben lennének)
        print(f"A(z) {csoport_letszam} fő osztálylétszámú osztályban {csoport_letszam//5} öt fős csapatot hozhatunk létre!")
    elif csoport_letszam % 5 <= 2: #ha egy, vagy két ember nem tudna egy őt fös csapat tagja lenni, akkor
                        #a csoport létszáma            #hány ötfős csapat jön létre (pl. 21 fő esetén 4 csapat)     #ha 1 emberrel vannak többen, akkor egy 6-fős csapat lesz, ha kettő ember van, akkor 2 szál be egy-egy csapatba
        print(f"A(z) {csoport_letszam} fő osztálylétszámú osztályban {csoport_letszam//5} csapatot hozhatunk létre, de {csoport_letszam%5} csapat hat fős lesz!")
    else: #minden más esetben, egy új csapat jön létre, tehát ha 3 vagy négy fő nem tud egy öt fős csapatba beszálni, ők egy külön csapatot alkotnak
                                                                    #lekerekíti, így +1-el növelnem kell (pl. 24/5=4.8, ezt lekerekíti 4-re, de plusz egy csapat lesz)
        print(f"A(z) {csoport_letszam} fő osztálylétszámú osztályban {csoport_letszam//5+1} csapatot hozhatunk létre, de az utolsó csapat csak {csoport_letszam%5} fős lesz!")
                                                                                                                                                    #a maradék megadja az utolsó csapat létszámát!


