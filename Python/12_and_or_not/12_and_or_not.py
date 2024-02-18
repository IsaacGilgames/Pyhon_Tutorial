#and_or_not.py

#True and True = True
#True and False = False
#False and True = False
#False and False = False

#True or True = True
#True or False = True
#False or True = True
#False or False = False

number1 = int(input("Adj meg egy számot!\n"))
number2 = int(input("Adj meg egy számot!\n"))

if number1 > 0 and number2 > 0:
    print("Mind a két szám pozitív!")
elif number1 > 0 or number2 > 0:
    print("Csak az egyik szám pozitív!")
    if number1 > 0:
        print("Az első szám a pozitív: %d" %(number1))
        #print("Az első szám a pozitív: " + str(number1))
        #print("Az első szám a pozitív:", number1)
        #print(f"Az első szám a pozitív: {number1}")
        #print("Az első szám a pozitív: {0}".format(number1))
    else:
        print("A második szám a pozitív: %d" %(number2))
else:
    print("Egyik szám sem pozitív!")


if number1 % 2 == 0 and number1 % 2 == 0:
    print("Mind a két szám páros!")
elif number1 % 2 == 0 or number2 % 2 == 0:
    print("Csak az egyik szám páros, vagyis", end=" ")
    if number1 % 2 == 0:
        print("vagyis az első szám, amely a(z) %d" %(number1))
    else:
        print("vagyis a második szám, , amely a(z) %d" %(number2))
else:
    print("Egyik szám sem páros!")
