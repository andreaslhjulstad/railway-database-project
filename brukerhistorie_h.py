""" For en bruker skal man kunne finne all informasjon om de kjøpene hen har gjort for fremtidige
reiser. Denne funksjonaliteten skal programmeres. """

from datetime import date
import sqlite3

con = sqlite3.connect("jernbaneDatabase.db")
cursor = con.cursor()

kundenummer = input("Skriv inn ditt kundenummer: ")
dagens_dato = date.today()
dato_formatert = dagens_dato.strftime("%Y-%d-%m")

cursor.execute("select * from (Kunde join Kundeordre using (kundenr)) join Billett using (ordrenr) where kundenr = ? and forekomstDato >= ?", (kundenummer, dato_formatert))

rows = cursor.fetchall()

for i in range(len(rows)):
    print(rows[i])

