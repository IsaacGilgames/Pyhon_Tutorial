#formatalas
epizod = 7
meghalt = "Han Solo :("
#a különálló részek külön paraméterként való megadása (vesszővel elválasztva)
#így nem zavarja a print fügvényt, hogy string, vagy float, vagy integer, vagy bool típusú érték van beírva
print("Star Wars", 7)
#szöveg összefűzés a + jel ebben az esetben
#a str() fügvény átalakítja az érték vagy a változó típusát stringgé, még ha egy számot is írtam be
print("Star Wars " + str(7))
print("Star Wars " + str(epizod))
#a részek formatálása, átalakítása és beillesztése a szövegbe
print("A Star Wars %d. részében meghalt %s" %(epizod, meghalt))
print("A Star Wars {0}. részében meghalt {1}" .format(epizod, meghalt))
print(f"A Star Wars {epizod}. részében meghalt {meghalt}")
