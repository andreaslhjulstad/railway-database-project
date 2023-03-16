""" For en stasjon som oppgis, skal bruker få ut alle togruter som er innom stasjonen en gitt ukedag.
Denne funksjonaliteten skal programmeres. """

import sqlite3
con = sqlite3.connect("jernbaneDatabase.db")

cursor = con.cursor()

success = 0 

while success == 0:
    stasjon = input("Velg stasjon: ").lower().title()
    ukedag = input("Velg ukedag: ").lower()

    gyldige_ukedager = ["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"]

    cursor.execute("select * from Togrutetabell join Driftsdager using (rutenr) where stasjon = ? and ukedag = ?", (stasjon, ukedag))

    rows = cursor.fetchall()

    print("\n")

    success = 0

    if ukedag in gyldige_ukedager: 
        if rows != []:
            print("Disse resultatene ble funnet for " + stasjon + " på " + ukedag + ":")
            print("Rutenummer, Stasjon, Ankomsttid, Avgangstid, Ukedag: ")
            for i in range(len(rows)):
                print(rows[i])
            success = 1
        else: 
            print("Stasjon eksisterer ikke! Venligst prøv igjen")
    else:
        print("Ukedag er ikke gyldig! Venligst prøv igjen")

con.close()