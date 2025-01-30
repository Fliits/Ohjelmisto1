def lasku(nlista):
    karsitut = []
    for n in nlista:
        if n % 2 != 0:
            nlista.remove(n)
        else:
            karsitut.append(n)
    return karsitut

luvut = []

syote_str = input("Anna luku: ")
while syote_str != "":
    syote = int(syote_str)
    luvut.append(syote)
    syote_str = input("Anna luku: ")
else:
    print(f"Listassa oli: {luvut}")
    parilliset = lasku(luvut)
    print(f"Parillisia olivat {parilliset}")