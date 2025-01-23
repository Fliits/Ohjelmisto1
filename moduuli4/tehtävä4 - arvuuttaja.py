import random
noppa = random.randint(1,6)
arvaus = 0

while arvaus != noppa:
    arvaus = int(input("Arvaa luku: "))
    if arvaus == noppa:
        print("Oikein!")
        break
    if arvaus < noppa:
        print("Noppa on suurempi")
    if arvaus > noppa:
        print("Noppa on pienempi")