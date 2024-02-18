print("Star", "Wars") #paraméterek
print("Star " + "Wars") #összefűzöm őket
print("Star", "Wars", 7)
#print("Star " + "Wars " + 7) szemantikus hiba
print("Star " + "Wars " + str(7))
print()
print("Egy", "Kettő", "Három", "Négy", sep=', ') #mivel legyenek egymástól elválasztva az elemek/elszeparálva
print("Egy", "Kettő", "Három", "Négy", sep='-')
print("Egy", "Kettő", "Három", "Négy", sep='\n') #\n sortörés
print("Egy", "Kettő", "Három", "Négy", end='\n\n') #end mi legyen a sor végén <-- példában itt két sortörés
print("Felettem és alattam is van két üres sor", end='\n\n')
print("""Ej, mi a kő! tyúkanyó, kend\\nA szobában\b \tlakik itt bent?\nLám, csak jó az isten, jót ád,\nHogy fölvitte a kend dolgát!""")
#\n -->sortörés
#\t -->tabulátor
#\b -->backspace
#\\n -->figyelmen kívül hagyja a fordított perjel utáni részt, nem lesz sortörés
#escape karakterek figyelmen kívül hagyása
print("Z:\biológia\nevek\témazáró") #szemantikai hiba, nem úgy írja, ki ahogy én szeretném
print(r"Z:\biológia\nevek\témazáró") #jó
print(R"Z:\biológia\nevek\témazáró") #jó
print(repr("Z:\biológia\nevek\témazáró")) #jó


