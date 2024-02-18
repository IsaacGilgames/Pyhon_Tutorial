t = ("name", "sex", "age", "weight", "height", "level", "testömeg index")
def imb(h, w):
    IMB = w / (h/100) ** 2
    return IMB

students = []
while True:
    name = input("Írd be a tanuló nevét: ")
    if name == "":
        break
    sex = input("Írd be a tanuló nemét: ")
    age = int(input("Írd be a tanuló nevét: "))
    weight = float(input('Add meg a tanuló súlyát (kg): '))
    height = float(input('Add meg a tanuló magasságát (cm): '))
    level = input('Add meg a tanuló csoportja (kezdő/haladó): ')

    s = [name, sex, age, weight, height, level,]
    students.append(s)
    students.append(imb(height, height))
    




