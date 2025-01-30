def muunna(i):
    litrat = i * 3.785
    return litrat

gallonat = int(input("Anna gallonat: "))

while gallonat >= 0:
    litra = muunna(gallonat)
    print(f"Litroina: {litra}")
    gallonat = int(input("Anna gallonat: "))
else:
    print("Negatiivinen luku, ei muunneta.")