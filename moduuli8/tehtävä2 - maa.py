import mysql.connector

def koodi(maa):
    sql = (f"SELECT type, count(*) FROM airport where iso_country='{maa}' group by type desc")
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        print(f"Tulostetaan lentokenttien määrä tyypeittäin:")
        for rivi in tulos:
            print(f"{rivi}.")
    return

yhteys = mysql.connector.connect(
        # host='localhost',
        # port= 3306,
         database='flight_game',
         user='pythonuser',
         password='salasana',
         autocommit=True
         )

syote = input("Anna maakoodi: ")
koodi(syote)