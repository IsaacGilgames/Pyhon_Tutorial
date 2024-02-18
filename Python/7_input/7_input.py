#input

print("Írd le a nevedet!")
name = input()
print("Szia", name, "!")
print("Szia", name + "!")
print("Szia", name + "!")
print("Szia ", name, "!", sep="")


x = None
y = None
print("Adj meg két számot!", 
"Figyelj arra, hogy csak egész számot adhatsz meg!"
, sep="\n")

x = int(input("Mi legyen az x értéke?\n"))
y = int(input("Mi legyen az y értéke?\n"))

#print(x + y)
osszeg = x + y
print(x, "+", y, "=", osszeg)


pi = 3.14
r = float(input("Add meg a kör sugarát (cm): "))
K = 2 * r * pi
print("A kör kerülete:", K, "cm")


a = None
b = None

a = int(input("Adj meg egy számot: "))
b = int(input("Adj meg egy számot: "))

print(a, b, sep="\n")
temp = a
a = b
b = temp
print(a, b, sep="\n")


number = 15
print("Legyen a number 4-gyel osztható!")
print("Number:", number)
hozzaad = int(input("Mit adjak hozzá?\n"))
number += hozzaad

print("Az új number érték, ami 4-gyel osztható: ", number)



