""" For en stasjon som oppgis, skal bruker få ut alle togruter som er innom stasjonen en gitt ukedag.
Denne funksjonaliteten skal programmeres. """

import sqlite3
con = sqlite3.connect("jernbaneDatabase.db")

cursor = con.cursor()

success = 0 

while success == 0:
    station = input("Velg stasjon: ").lower().title()
    weekday = input("Velg ukedag: ").lower()

    valid_weekdays = ["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"]

    cursor.execute("select rutenr, ankomsttid, avgangstid from Togrutetabell join Driftsdager using (rutenr) where stasjon = ? and ukedag = ?", (station, weekday))

    rows = cursor.fetchall()

    print("\n")

    success = 0

    if weekday in valid_weekdays: 
        if rows != []:
            print("Disse resultatene ble funnet for " + station + " på " + weekday + ":")
            print("Rutenummer, Ankomsttid, Avgangstid: ")
            for i in range(len(rows)):
                print(rows[i])
            success = 1
        else: 
            print("Stasjon eksisterer ikke! Vennligst prøv igjen")
    else:
        print("Ukedag er ikke gyldig! Vennligst prøv igjen")

con.close()