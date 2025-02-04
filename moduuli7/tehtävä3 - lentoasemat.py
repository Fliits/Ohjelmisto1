lentoasemat = {"EFHK":"Helsinki-Vantaan lentoasema"}

def haku():
        haku = input("Anna ICAO-koodi: ")
        if haku in lentoasemat:
            print(f"Aseman nimi on {lentoasemat[haku]}.")
def lista():
        koodi = input("Anna aseman ICAO-koodi: ")
        asema = input("Anna aseman nimi: ")
        lentoasemat[koodi] = asema

syote = input("Anna komento (syötä/hae/lopeta):")
while syote != "lopeta":
    while syote == "hae":
        haku()
        syote = input("Anna komento (syötä/hae/lopeta):")
    while syote == "syötä":
        lista()
        syote = input("Anna komento (syötä/hae/lopeta):")