#fuggvenyek.py

#print()
a = 2024
b = "Boldog Újévet!"
def valami(kiirni):                       #def függvénye_neve(paraméter)
    print(kiirni)

valami(a)
valami(b)

#def paros_paratlan(x, par):
#    print(f"A(z) {x} szám {par}!")

def milyen_szam(x, text):
    print(f"A(z) {x} szám {text}!")

number = int(input("Adj meg egy számot!\n"))

if number % 2 == 0:
    milyen_szam(number, "páros")
else:
    milyen_szam(number, "páratlan")

if number < 0:
    milyen_szam(number, "negatív")
elif number == 0:
    milyen_szam(number, "nulla")
else:
    milyen_szam(number, "pozitív")

