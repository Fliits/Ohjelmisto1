import random

sluku = 0

def noppa(suurin):
    luku = random.randint(1, suurin)
    return luku

haluttu = int(input("Nopan enimmäissilmäluku on: "))

while sluku != haluttu:
    sluku = noppa(suurin = haluttu)
    print(f"Nopan heitto on: {sluku}")
else:
    print(f"Nopan heitto on {haluttu}!")