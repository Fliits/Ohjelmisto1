import random

nopat = int(input("Anna noppien määrä: "))
tulot = []
toistot = summa = 0

while toistot < nopat:
    noppa = random.randint (1,6)
    tulot.append(noppa)
    toistot = toistot + 1
else:
    print(tulot)
    for n in tulot:
        summa = summa + n
    print(summa)