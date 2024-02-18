#rj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre, hogy
#három különböző értéket kapott-e!

#Első megoldás
szam1 = float(input("Kérem, adjon meg egy számot: "))
szam2 = float(input("Kérem, adjon meg még egy számot: "))
szam3 = float(input("Kérem, adjon meg egy harmadik számot: "))

if szam1 != szam2 and szam1 != szam3 and szam2 != szam3:
    print("A megadott három szám különböző értékeket képvisel.")
else:
    print("Legalább két szám azonos értékű, kérlek adjon meg három különböző számot.")


#Második megoldás
a = float(input("Szam1: "))
b = float(input("Szam2: "))
c = float(input("Szam3: "))

if a == b and a != c:
    print(f"A {a} és a {b} egyezik de a {c} nem")
elif b == c and b != a:
    print(f"A {b} és a {c} egyezik de a {a} nem")
elif c == a and c != b:
    print(f"A {c} és a {a} egyezik de a {b} nem")
else:
    print(f"Mindegyik egyezik! ({a} = {b} = {c})")



#Harmadik megoldás
def fo(nums):
    if len(set(nums)) == len(nums):
        print("mindegyik kulonbozik")
    else:
        print("nem mindegyik kulonbozik")

try:
    nums = []

    for i in range(3):
        num = float(input(f"adj meg egy szamot: "))
        nums.append(num)

    fo(nums)

except ValueError:
    print("hibas megadott szam")