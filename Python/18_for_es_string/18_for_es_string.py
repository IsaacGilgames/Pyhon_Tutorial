text = "árvíztűrő tükörfúrógép"

for i in range(len(text)):
    print(text[i])

for ig in range(len(text)):
    print(text[:ig+1])

for char in text:   #char (bármilyen név lehet ez) ez mindig az aktuális karaktert tárolja el, 
    print(char)     #vagyis a szövegen karakterenként megyek végig
        
for i in range(0, len(text)):           #a szöveg helyén * jelenik meg
    #print("*", end="")
    cenzura = cenzura + "*"
print(cenzura)
