tura = 12350
napikm = 30
nap = tura//napikm
if tura % napikm == 0:
    print(f"A(z) {tura} km-t összesen {tura//napikm} nap alatt teszem meg!")
elif tura % napikm < 10:
    print(f"A(z) {tura} km-t összesen {tura//napikm} nap alatt teszem meg, de utolsó nap {tura%napikm+30}!")
else:
    print(f"A(z) {tura} km-t összesen {tura//napikm+1} nap alatt teszem meg, de utolsó nap {tura%napikm}!")