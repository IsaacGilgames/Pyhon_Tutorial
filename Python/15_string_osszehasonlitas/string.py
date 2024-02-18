#string

szoveg1 = "Ődön"                        #kis és nagybetű között különbséget tesz!
szoveg2 = "ödön"
szoveg3 = "12"
szoveg4 = ""
number = 12
print(szoveg1 == szoveg2)               #Output: False
if szoveg1 == szoveg2:                  #a kis és nagybetűk között különbséget teszünk
    print("Ugyanaz a két szó!")
else:
    print("Nem ugyanaz a két szó!")

if szoveg1 == szoveg2.lower():       #.lower() minden betűt kisbetűssé alakít
    print("Ugyanaz a két szó!")
else:
    print("Nem ugyanaz a két szó!")


if szoveg3 == number:
    print("Ugyanaz a két dolog!")
else:
    print("Nem ugyanaz a két dolog!")


if szoveg3:
    print("Van-e szövegem!")

if szoveg4:
    print("Van-e szövegem!")

if number:
    print("Nem nulla a számom!")

