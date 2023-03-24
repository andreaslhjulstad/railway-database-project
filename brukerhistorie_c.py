""" For en stasjon som oppgis, skal bruker få ut alle togruter som er innom stasjonen en gitt ukedag.
Denne funksjonaliteten skal programmeres. """

import sqlite3

# Oppretter tilkobling til databasen
con = sqlite3.connect("jernbaneDatabase.db")
cursor = con.cursor()

# Lager en variabel for å sjekke om programmet er ferdig
success = 0

# Løkke som kjører fram til begge brukerinputene er validert og returnerer utskriften
while success == 0:
    station = input("Velg stasjon: ").lower().title()
    weekday = input("Velg ukedag: ").lower()

    # Oversikt over gyldige ukedager
    valid_weekdays = ["mandag", "tirsdag", "onsdag",
                      "torsdag", "fredag", "lørdag", "søndag"]

    cursor.execute(
        "select rutenr, ankomsttid, avgangstid from Togrutetabell join Driftsdager using (rutenr) where stasjon = ? and ukedag = ?", (station, weekday))

    rows = cursor.fetchall()

    print("")

    success = 0

    # Sjekker om ukedagen er gyldig og om stasjonen er i databasen
    if weekday in valid_weekdays:
        if rows != []:
            print("Disse resultatene ble funnet for " +
                  station + " på " + weekday + ":")
            print("Rutenummer, Ankomsttid, Avgangstid: ")
            for i in range(len(rows)):
                print(rows[i])
            success = 1
        else:
            print("Stasjon eksisterer ikke! Vennligst prøv igjen")
    else:
        print("Ukedag er ikke gyldig! Vennligst prøv igjen")

# Lukker databasen
con.close()
