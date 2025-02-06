import mysql.connector
from geopy import distance

def koodi(icao1, icao2):
    sql1 = (f"SELECT name, latitude_deg, longitude_deg FROM airport where ident='{icao1}'")
    sql2 = (f"SELECT name, latitude_deg, longitude_deg FROM airport where ident='{icao2}'")
    print(sql1, sql2)

    kursori = yhteys.cursor()
    kursori.execute(sql1)
    tulos1 = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos1:
            print(f"Koodi kuuluu lentokentälle {rivi}.")
            paikka1 = rivi[1], rivi[2]

    kursori.execute(sql2)
    tulos2 = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos2:
            print(f"Koodi kuuluu lentokentälle {rivi}.")
            paikka2 = rivi[1], rivi[2]

    print(distance.distance(paikka1, paikka2).km)
    return

yhteys = mysql.connector.connect(
        # host='localhost',
        # port= 3306,
         database='flight_game',
         user='pythonuser',
         password='salasana',
         autocommit=True
         )

eka = input("Anna ICAO-koodi: ")
toka = input("Anna toinen ICAO-koodi: ")
koodi(eka, toka)