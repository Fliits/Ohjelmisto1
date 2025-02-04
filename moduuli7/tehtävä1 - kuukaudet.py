kuukaudet = ("Tammikuu", "Helmikuu", "Maaliskuu", "Helmikuu", "Toukokuu", "Kesäkuu",
             "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Maaliskuu", "Joulukuu")
vuodenajat = "Talvi", "Kevät", "Kesä", "Syksy"
kuukausi = int(input("Anna kuukauden järjestysnumero (1-12): "))

if kuukausi == 12 or kuukausi == 1 or kuukausi == 2:
    print(f"{kuukausi}. kuukausi, {kuukaudet[kuukausi-1]}, on vuodenajassa {vuodenajat[0]}.")
elif kuukausi == 3 or kuukausi == 4 or kuukausi == 5:
    print(f"{kuukausi}. kuukausi, {kuukaudet[kuukausi-1]}, on vuodenajassa {vuodenajat[1]}.")
elif kuukausi == 6 or kuukausi == 7 or kuukausi == 8:
    print(f"{kuukausi}. kuukausi, {kuukaudet[kuukausi-1]}, on vuodenajassa {vuodenajat[2]}.")
elif kuukausi == 9 or kuukausi == 10 or kuukausi == 11:
    print(f"{kuukausi}. kuukausi, {kuukaudet[kuukausi-1]}, on vuodenajassa {vuodenajat[3]}.")
