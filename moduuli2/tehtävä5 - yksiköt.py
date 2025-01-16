lukuA = int(input("Anna leiviskät: "))
lukuB = int(input("Anna naulat: "))
lukuC = int(input("Anna luodit: "))

Luodit = lukuC * 13.3
Naulat = lukuB * 32 * 13.3
Leiviskat = lukuA * 20 * 32 * 13.3

Kilot = int((Leiviskat + Naulat + Luodit)/1000)
Grammat = (Leiviskat + Naulat + Luodit)%1000

print(f"Massa nykymittojen mukaan: {Kilot} kilogrammaa ja {Grammat:.2f} grammaa.")