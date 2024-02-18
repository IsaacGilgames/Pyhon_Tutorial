#lista.py
bevasarlo_lista = ["tojás", "alma", "hal eledel", "nesquik"]
print(bevasarlo_lista)

#print() type() int() range()
#.lower() .isnumeric() .count()

bevasarlo_lista.append("tejföl") #legvégére illeszti be
print(bevasarlo_lista)

bevasarlo_lista.pop() #legvégéről törli
print(bevasarlo_lista)


#bevasarlo_lista.clear() #törli a lista tartalmát!
#print(bevasarlo_lista)
bevasarlo_lista.append("alma")
bevasarlo_lista.append("alma")
bevasarlo_lista.remove("alma")  #törli, de csak az első előfordulását
print(bevasarlo_lista)

almak_szama = bevasarlo_lista.count("alma") #megszámolja
print(almak_szama)

i = bevasarlo_lista.index("nesquik")    #megjondja az indexét (fontos, hogy az első találatét)
print(i)

bevasarlo_lista.insert(2, "kalács")         #a listához hozzáadja, de egy meghatározott helyhez. A többit pedig egyel odébb tolja
print(bevasarlo_lista)

bevasarlo_lista.pop(1)  #"hal eledel"-t vágom ki, tehát az első indexű elemet
print(bevasarlo_lista)

bevasarlo_lista.reverse()   #megfordítja a listát
print(bevasarlo_lista)

bevasarlo_lista.sort()  #sorba rendezi a listát (abc vagy növekvő)
print(bevasarlo_lista)










