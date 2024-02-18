bajnoksag_eve = [
    1982,
    1986,
    1990,
    1994,
    1998,
    2002,
    2006,
    2010,
    2014, 
    2018,
    2022
]

bajnoksag_gyoztes = [
    "Olaszország",
    "Argentína",
    "Németország",
    "Brazília",
    "Franciaország",
    "Brazília",
    "Olaszország",
    "Spanyolország",
    "Németország",
    "Franciaország",
    "Argentína"
]

ev = int(input("Volt-e abban az évben bajnokság?\n"))
helyes = False
for b_eve in bajnoksag_eve:
    if b_eve == ev:
        helyes = True

if helyes == True:
    print("Abban az évben volt bajnoság!")
else:
    print("Abban az évben nem volt bajnoság!")

for i in range(0, len(bajnoksag_eve)):
    if bajnoksag_eve[i] == ev:
        print(f"{ev}-ben a bajnok: {bajnoksag_gyoztes[i]}")
        