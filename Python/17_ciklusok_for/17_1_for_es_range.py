#for -> ciklus

#c++ for(int i = 0; i < 10; i++) {}
#javascript for(let i = 0; i < 10; i++) {}


print(range(10))        #range(kezdőérték, végérték, lépés) <- sorozat

for i in range(10): #adott alkalommal ismétli meg <- (0 <= i < 10)
    print(i)

for j in range(10, 21):  ##adott alkalommal ismétli meg <- (10 <= i < 21)
    print(i)

for i in range(1, 10, 2): #kezdő érték, meddig megyek, hányasával lépked, (1 <= i < 10)
    print(i)


for i in range(5,100+1,5):  #5-től 100-ig kiírja a számokat
    print(i, end="; ")      #az end hatására felülirtuk a sortörést és egymás mellé kerülnek

