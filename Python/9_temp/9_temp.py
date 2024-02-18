#temp -> ideiglenes változo pl. két érték kicseréléséhez
#a neve természetesen bármi lehet, de a hivatalos példákban is ez szokot lenni temporary, vagyis magyarul ideiglenes

a = None
b = None
a = int(input("Adj meg egy számot: "))
b = int(input("Adj meg egy számot: "))
print(a)
print(b)
temp = a
a = b
b = temp
print(a)
print(b)
