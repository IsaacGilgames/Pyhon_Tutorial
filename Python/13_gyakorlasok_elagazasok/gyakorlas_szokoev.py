#Határozd meg egy adott évről, hogy az szökőév lehetett-e!
#Ha egy év osztható 400-al, vagy egy év osztható 4-el, de nem osztható 100-al, akkor szökőév!

ev = int(input("Adj meg egy évet: "))
szokoev = False

#Első
if ev % 400 == 0:
    szokoev = True
elif ev % 4 == 0 and ev % 100 != 0:
    szokoev = True
else:
    szokoev = False

if szokoev==True:
    #print(ev, "szököév volt!")
    #print(str(ev) + " szököév volt!")
    #print("%d szököév volt" %(ev))
    print(f"{ev} szököév volt!")                #Itt több féle kiírattatást láthatsz!
    #print("{0} szököév volt".format(ev))
else:
    print(f"A megadott {ev} év nem volt szököév!")

#Második megoldás
if (ev % 400 == 0) or (ev % 4 == 0 and ev % 100 != 0):
    print(f"{ev} szököév volt!")
else:
    print(f"A megadott {ev} év nem volt szököév!")