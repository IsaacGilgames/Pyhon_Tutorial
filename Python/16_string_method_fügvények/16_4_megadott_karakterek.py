#megadott_karakter.py

text = "árvíztűrő tükörfúrógép"
#       0123456789
text2 = "turó rudi"

print(text)
print(len(text))
print(text.count("r"))  #Megszámolja hány "r" van a karakterláncban

print(text.find("r")) #hányadik helyen van, sorszámát/indexét adja vissza. Fontos, hogy csak az első találatét
print(text.rfind("r"))  #az utolsó találat indexét adja vissza
print(text.index("az"))
print(text.rindex("r"))

print(text.find("ár")) #nem csak karakterekkel működik


print(text.startswith("kezdtek"))   #ezzel kezdődik-e?
print(text.endswith("p"))           #ezzel végződik-e?



print(text[8])      #a 9. indexő karaktert adja vissza (itt az "ő" betüt)
print(text[0:4])   #a karakter egy részét
print(text[:9])     #árvíztűrő <- elejétő a 9. indexő elemig
print(text[10:])    #tükörfúrógép <- megadott helytől a végéig

#utolsó karakter megadása
print(text[len(text)-1])      #megadja a karakterek számát, és az utolsó karakter indexe mindig egyel kevesebb
print(text[-1])                #egyszerűbb, de a másik több helyen használható


