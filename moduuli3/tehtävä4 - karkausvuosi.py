vuosi = int(input("Anna vuosiluku: "))

vuosi1 = float(vuosi%4)
vuosi2 = float(vuosi%400)
vuosi3 = float(vuosi%100)

if vuosi1==0 and vuosi2==0 and vuosi3==0:
    print("Vuosi on karkausvuosi.")
elif vuosi1==0 and vuosi2!=0:
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")