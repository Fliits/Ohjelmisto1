def lasku(nlista):
    summa = 0
    for n in nlista:
        summa = summa + n
    print(f"Lukujen summa on: {summa}")
    return summa

luvut = []

syote_str = input("Anna luku: ")
while syote_str != "":
    syote = int(syote_str)
    luvut.append(syote)
    syote_str = input("Anna luku: ")
else:
    lasku(luvut)