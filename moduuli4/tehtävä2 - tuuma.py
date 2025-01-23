tuumat = float(input("Anna tuumat: "))
while tuumat >= 0:
    sentit = tuumat * 2.54
    print(f'Senttimetreinä: {sentit:.2f}')
    tuumat = float(input("Anna tuumat: "))
print('Luku negatiivinen, toiminta keskeytetty.')