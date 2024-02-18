#ciklus_gyakorlas
"""
print(" " * 2 + "*" * 7)
print(" "+ "*********")
print("***********")
"""
utolso = int(input("Mekkora legyen a karácsonyfa?"))
szokoz = utolso // 2
for i in range(1, utolso+1, 2):      #1 <= i < 23
    print(" " * szokoz + "*"*i)
    szokoz -= 1
