#Döntsd el a háromszög három oldala alapján (cm-ben adjuk meg mindet), 
# hogy derékszögű háromszög-e!
#Irattasd ki, hogy melyik oldal az átfogó, és melyik oldalak a befogók!
#Pl.
#A derékszögű háromszög befogói a(z) 24 cm és 18 cm, míg az átfogója 
# a(z) 30 cm.
#A megadott értékek alapján ez nem lehet derékszögű háromszög

a = float(input("Add meg a háromszög egyik oldalát: "))
b = float(input("Add meg a háromszög egyik oldalát: "))
c = float(input("Add meg a háromszög egyik oldalát: "))

if a**2 + b**2 == c**2:
    print(f"A derékszögű háromszög befogói a(z) {a} cm és {b} cm, míg az átfogója  a(z) {c} cm.")
elif a**2 + c**2 == b**2:
    print(f"A derékszögű háromszög befogói a(z) {a} cm és {c} cm, míg az átfogója  a(z) {b} cm.")
elif c**2 + b**2 == a**2:
    print(f"A derékszögű háromszög befogói a(z) {c} cm és {b} cm, míg az átfogója  a(z) {a} cm.")
else:
    print("A megadott oldalakkal ez nem lehet derékszögű háromszög!")