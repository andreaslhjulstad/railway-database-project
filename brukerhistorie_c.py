""" For en stasjon som oppgis, skal bruker få ut alle togruter som er innom stasjonen en gitt ukedag.
Denne funksjonaliteten skal programmeres. """

import sqlite3
con = sqlite3.connect("jernbaneDatabase.db")

cursor = con.cursor()

stasjon = input("Velg stasjon: ").lower().title()
ukedag = input("Velg ukedag: ").lower()

cursor.execute("select rutenr, avgangstid from Togrutetabell join Driftsdager using (rutenr) where stasjon = ? and ukedag = ?", (stasjon, ukedag))

rows = cursor.fetchall()

print("\n")
print("Disse resultatene ble funnet for " + stasjon + " på " + ukedag + ":")
print("Rutenummer, Avgangstid: ")
for i in range(len(rows)):
    print(rows[i])

con.close()