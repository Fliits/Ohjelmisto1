luvut = []
luku_str = input("Anna luku: ")
while luku_str != '':
    luku = int(luku_str)
    luvut.append(luku)
    luku_str = input("Anna luku: ")
luvut.sort(reverse=True)
print(luvut)
for index in range(0, 5):
    print(luvut[index])