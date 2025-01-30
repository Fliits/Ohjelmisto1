def pizza(koko, hinta):
    suhde = koko / hinta
    return suhde

ekakoko = int(input("Anna pizzan koko (senttimetreinä): "))
ekahinta = int(input("Anna pizzan hinta (euroina): "))
tokakoko = int(input("Anna toisen pizzan koko (senttimetreinä): "))
tokahinta = int(input("Anna pizzan hinta (euroina): "))
eka = pizza(ekakoko, ekahinta)
toka = pizza(tokakoko, tokahinta)
if eka > toka:
    print("Ensimmäinen pizza on parempi vastine rahalle.")
if toka > eka:
    print("Toinen pizza on parempi vastine rahalle.")