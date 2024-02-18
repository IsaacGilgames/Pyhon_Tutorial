"""
A programban olvass be egy nevet a konzolról és külön sorokba írd ki:
- csupa nagybetűvel
- csupa kisbetűvel
- szélső szóközök nélkül
- hány "a" betű van benne
- hány betűből áll
- a 3. betűje
- az utolsó előtti betűje
- az első három betűje
- az utolsó három betűje
- 7-9. betűi
- Szia név! Örülök, hogy itt vagy.
"""

nev = input("Kérem, adja meg a nevét: ")

print("Csupa nagybetűvel:")
print(nev.upper())

print("\nCsupa kisbetűvel:")
print(nev.lower())

print("\nSzélső szóközök nélkül:")
print(nev.strip())

print(f"\nHány 'a' betű van benne: {nev.lower().count('a')}")

print(f"\nHány betűből áll: {len(nev)}")

print(f"\nA 3. betűje: {nev[2]}")

print(f"\nAz utolsó előtti betűje: {nev[-2]}")

print(f"\nAz első három betűje: {nev[:3]}")

print(f"\nAz utolsó három betűje: {nev[-3:]}")

print(f"\n7-9. betűi: {nev[6:9]}")

print(f"\nSzia {nev}! Örülök, hogy itt vagy.")