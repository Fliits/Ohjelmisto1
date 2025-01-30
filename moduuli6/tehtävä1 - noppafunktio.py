import random

sluku = 0

def noppa():
    luku = random.randint(1, 6)
    return luku

while sluku != 6:
    sluku = noppa()
    print(f"Nopan heitto on: {sluku}")
else:
    print("Nopan heitto on kuusi!")