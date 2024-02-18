#ugyanaz.py

numbers1 = [2, 1, 4, 2, 3, 2, 3, 5]
numbers2 = [3, 4, 7, 4, 2, 1]
numbers3 = [3, 4, 4, 4, 3, 12, 21, 12, 21, 5, 4]
def ismetlodes(numbers):
    megtalalt = []
    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                if numbers[i] not in megtalalt:
                    megtalalt.append(numbers[i])
                    print(f"{numbers[i]} ismétlődik")

print("1. lista")
ismetlodes(numbers1)
print()
print("2. lista")
ismetlodes(numbers2)
print()
print("3. lista")
ismetlodes(numbers3)
print()