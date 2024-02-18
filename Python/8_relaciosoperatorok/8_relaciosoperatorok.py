#relaciosoperatorok.py
#boolean operátoroknak is nevezzük
#>
#<
#<=
#>=
#==
#!=

print(2>2) #False
print(2 < 5) #True
print(14 == 14) #True
print(14 != 15) #True


#Játszom egy játékkal pár perce
#Csak a másodpercet tudom
#Döntsük el, hány perce és 
#hány másodperce játszom
#5 percnél régebb óda játszom-e

game_second = int(input("Hány másodperce játszom?\n"))
tobb_mint_5 = game_second / 60 > 5.0
game_minute = game_second // 60
game_second %= 60
print(game_minute, "perc")
print(game_second, "másodperc")
print("Több, mint 5 perce játszom: ", tobb_mint_5)

