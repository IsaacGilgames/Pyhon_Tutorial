#ékezetes magánhangzók kicserélése ékezetmentesre
text = "Árvíztűrő tükörfúrógép"
text = text.lower()
print(len(text))
for i in range(len(text)-1):
    #print(text[i])
    if text[i] == "á":
        text = text.replace("á", "a")
    elif text[i] == "é":
        text = text.replace("é", "e")
    elif text[i] == "í":
        text = text.replace("í", "i")
    elif text[i] == "ő" or text[i] == "ö" or text[i] == "ó":
        text = text.replace(text[i], "o")
    elif  text[i] == "ű" or text[i] == "ü" or text[i] == "ú":
        text = text.replace(text[i], "u")
print(text)