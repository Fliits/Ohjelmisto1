luku = int(input("Anna luku: "))

for i in range(2, luku):
    if luku % i == 0:
        print("LUKU EI OLE ALKULUKU")
        break
else:
    print("LUKU ON ALKULUKU")
