print("egyenlo szaru haromszog")
for i in range(1, 30):
    print("* " * i)

print("\n\n")
for i in range(1, 30):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

for i in range(29, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


