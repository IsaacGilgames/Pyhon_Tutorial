nem = ""

nem = input("Adja meg a nemét!\n")

while nem != "férfi" and nem != "fiú" and nem != "nő" and nem != "lány":
    nem = input("Adja meg a nemét!\n")

print(f"A te nemed: {nem}")

#Később még tanuljuk pontosan a következő operátorokat: is, is not, in, in not 

nem = ""
nemek = ["férfi", "fiú", "nő", "lány"]
nem = input("Mi a nemed?\n")

while nem not in nemek:
    nem = input("Mi a nemed?\n")
