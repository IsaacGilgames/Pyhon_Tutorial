#tipuskenyszerites_tipuskonverzio.py
a = 23 #integer
b = 45.125 #float
c = "True" #string
d = True #bool

print(a, b, c, d, sep="\n\n", end="\n\nMind ugyan úgy néz ki\n")

print(a)
print(23)
print(a == 23) #igaz

print("23")
print(a == "23")

valtozo = 10
print(type(valtozo))
valtozo = 20.5
print(type(valtozo))
valtozo = "valami"
print(type(valtozo))
valtozo = True

"""
answer = int(input("Írj be egy számot:"))
print(answer)
print(type(answer))
print(int(answer) < 10)
print(type(answer))
"""
x = 12
y = 5
#12+5=17
print("Összeadás: ", end="")
print(str(x), "+", str(y), "=", x+y, sep="")
print(x, "+", y, "=", x+y, sep="")
#print(x + "+" + y + "=", x+y, sep="")
print(str(x) + "+" + str(y) + "=", x+y, sep="")


