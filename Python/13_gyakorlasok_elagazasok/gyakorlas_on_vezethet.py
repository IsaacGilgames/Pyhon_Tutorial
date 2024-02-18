#Ön vezethet-e?

#Jogosítvány <- igaz
#Alkoholt nem fogasztottam

jogsi = None
alkoholt_ittam = None

jogsi =  input("Van-e jogsid? (igen/nem)\n")
#input -> int(), float(), bool(), str()
#jogsi =  bool(input("Van-e jogsid? (True/False)\n"))
alkoholt_ittam =  input("Ittam ma már alkoholt az elmúlt 8 órában? (igen/nem)\n")

if jogsi.casefold() == "igen":
    if alkoholt_ittam == "nem":
        print("Vezethetek!")
    else:
        print("Nem vezethetek!")
else:
    print("Nem vezethetek!")
