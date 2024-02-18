t = ("Név: ", "Nem: ", "Kor: ", 
"Súly (kg): ", "Magasság (cm): ", 
"Csoport: ", "Testömeg index: ")
students = []

def bmi():
    BMI = weight / ((height / 100) ** 2)
    print("A testömeg index: ", round(BMI, 2))
    return round(BMI, 2)

def makeItList(column):
    row = len(students)
    lista = []
    for i in range(row):
        lista.append(students[i][column])


while True:
    name = input('Add meg a tanuló nevét: ')
    if name == "":
        break
    sex = input('Add meg a tanuló nemét: ')
    age = int(input('Add meg a tanuló életkorát: '))
    weight = float(input('Add meg a tanuló súlyát (kg): '))
    height = float(input('Add meg a tanuló magasságát (cm): '))
    level = input('Add meg a tanuló csoportja (kezdő/haladó): ')

    student = [name, sex, age, weight, height, level]
    student.append(bmi())
    students.append(student)

print(max())
print(max())









