import mysql.connector

def koodi(icao):
    sql = f"SELECT name FROM airport where ident='{icao}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"Koodi kuuluu lentokentälle {rivi}.")
    return

yhteys = mysql.connector.connect(
        # host='localhost',
        # port= 3306,
         database='flight_game',
         user='pythonuser',
         password='salasana',
         autocommit=True
         )

syote = input("Anna ICAO-koodi: ")
koodi(syote)