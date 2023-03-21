""" Registrerte kunder skal kunne finne ledige billetter for en oppgitt strekning på en ønsket togrute
og kjøpe de billettene hen ønsker. Denne funksjonaliteten skal programmeres.
• Pass på at dere bare selger ledige plasser """


import sqlite3
import datetime
import brukerhistorie_d

# Opprett tilkobling til databasen
con = sqlite3.connect("jernbaneDatabase.db")
cursor = con.cursor()

# Henter lagrede jernbanestasjoner (for validering)
cursor.execute("SELECT navn FROM Jernbanestasjon")
rows = cursor.fetchall()
saved_stations = []
for row in rows:
    saved_stations.append(row[0])

# Henter registrerte e-postadresser:
cursor.execute("SELECT epost FROM Kunde")
email_array = cursor.fetchall()

# Henter inn e-postadresse fra bruker:
email = input("Skriv inn din email: ")
while not email in email_array[0]:
    email = input("Skriv inn din email: ")

# Finner kundenummer til bruker gitt email:
cursor.execute("SELECT kundenr FROM Kunde WHERE epost = ?", (email,))
customer_no = cursor.fetchall()[0][0]

# Henter inn start- og endestasjon fra brukerinput, og sjekker at de er gyldige:
start_station = input("Skriv inn en startstasjon: ").lower().title()

while not start_station in saved_stations:
    start_station = input("Skriv inn en startstasjon: ").lower().title()

end_station = input(
    "Skriv inn en endestasjon (må være forskjellig fra startstasjon): ").lower().title()

while not end_station in saved_stations or end_station == start_station:
    end_station = input(
        "Skriv inn en endestasjon (må være forskjellig fra startstasjon): ").lower().title()

# TODO: Legg til beskrivende kommentar
def get_next_ticketno():
    cursor.execute("SELECT billettnr FROM Billett")
    rows = cursor.fetchall()

    max_ticketno = 0
    for row in rows:
        if row[0] > max_ticketno:
            max_ticketno = row[0]
    return max_ticketno + 1

# TODO: Legg til beskrivende kommentar
def get_next_orderno():
    cursor.execute("SELECT ordrenr FROM Kundeordre")
    rows = cursor.fetchall()

    max_orderno = 0
    for row in rows:
        if row[0] > max_orderno:
            max_orderno = row[0]
    return max_orderno + 1


# Henter alle togrutenummer:
cursor.execute("SELECT rutenr FROM Togrute")
route_numbers = cursor.fetchall()

# Liste for togruter med oppgitt strekning, samt liste over alle stasjoner mellom start- og endestasjon:
train_routes = []
stations_in_between = []
route_stations_in_between_dict = {}

# Itererer gjennom alle togruter
for i in range(len(route_numbers)):
    # Henter alle stasjoner på ruten, samt deres stasjonsnr
    cursor.execute("SELECT * FROM Togrutetabell WHERE rutenr = ?", (str(route_numbers[i][0]),))
    stationQuery = cursor.fetchall()

    stations = []
    stationno = []
    stations_dict = {}

    # Lager map mellom stasjoner og deres stasjonnr
    for row in stationQuery:
        stations.append(row[1])
        stationno.append(row[4])

    stations_dict = {stations[j]: stationno[j] for j in range(len(stations))}
    
    # Sjekker om start- og endestasjonen er i togruten:
    if ((start_station in stations) and (end_station in stations)):
        # Sjekker at endestasjon kommer etter startstasjon:
        if stations_dict[end_station] > stations_dict[start_station]:
            train_routes.append(route_numbers[i][0])

            # Hvis det finnes mellomstasjoner på strekningen, legg dem til i en egen liste:
            for l in range(len(stations)):
                #print(str([stations[l]]))
                if (([stations_dict[stations[l]]][0] > stations_dict[start_station]) and ([stations_dict[stations[l]]][0] < stations_dict[end_station])):
                    #print("Stasjon " + str(stations[l]) + " er imellom!")
                    stations_in_between.append(stations[l])
            
            # Lager en mapping mellom hvert togrutenummer og tilhørende mellomstasjoner:
            route_stations_in_between_dict.update({route_numbers[i][0]:  stations_in_between})
            # Tømmer mellomstasjoner før neste iterering:
            stations_in_between = []

# Hvis ingen togruter inneholder oppgitt strekning, informer bruker:
avaliable_routes = len(train_routes)
if (avaliable_routes == 0):
    print("Ingen registrert togrute for strekning '" + start_station + "' til '" + end_station + "'!")
else:
    # Skriver ut hvilke togruter bruker kan velge mellom (må endres til å være mer brukervenlig):
    print("Mulige togruter for strekning: ")
    for k in range(avaliable_routes):
        print("Togrute nr. " + str(train_routes[k]))

    # Henter ønsket togrutenummer fra bruker:
    routenr = input("Velg én togrute: ").lower().title()
    while not int(routenr) in train_routes:
        routenr= input(
            "Velg én togrute: ").lower().title() 
    print("Du har valgt togrute " + str(routenr))

    # Henter datoer for forekomster på den oppgitte togruta:
    valid_dates = []
    cursor.execute("SELECT * FROM Togruteforekomst WHERE rutenr = ?", (str(routenr),))
    avaliable_dates = cursor.fetchall()
    # Hvis det ikke finnes noen forekomster, informer bruker:
    if (len(avaliable_dates) == 0):
        print("Det er dessverre ingen registrerte forekomster av den oppgitte togruten for øyeblikket. Prøv igjen senere.")
    else:
        date_today = datetime.date.today()
        for i in range(len(avaliable_dates)):
            date_element = str(avaliable_dates[i][0])
            year, day, month = date_element.split("-")
            date = datetime.date(int(year), int(month), int(day))
            if (date >= date_today):
                valid_dates.append(date.strftime("%Y-%d-%m"))

    # Hent ønsket dato fra bruker og sjekk at den er gyldig:
    print("\n")
    print("Gyldige datoer for reisen:", end=" ")
    for valid_date in valid_dates:
        print(valid_date, end="")
        if (valid_dates.index(valid_date) != len(valid_dates) - 1):
            print(",", end=" ")

    print("\n")
    chosen_date = input("Skriv inn datoen du vil reise på formatet 'YYYY-DD-MM': ")
    while not brukerhistorie_d.date_valid(chosen_date):
        chosen_date = input("Skriv inn datoen du vil reise på formatet 'YYYY-DD-MM': ")
    
    while chosen_date not in valid_dates:
        chosen_date = input("Skriv inn datoen du vil reise på formatet 'YYYY-DD-MM': ")

    # Konverterer den valgte forekomstdatoen til gyldig format for databasen:
    year, day, month = chosen_date.split("-")
    date = datetime.date(int(year), int(month), int(day))
    
    # Henter mulige vogner for togruten:
    cursor.execute("SELECT vognID, type FROM Togrute JOIN VognIOppsett USING (oppsettID) JOIN Vogn USING (vognID) WHERE rutenr = ?", (str(routenr),))
    wagons = cursor.fetchall()
    wagon_types = {}
    for wagon in wagons:
        wagon_types[wagon[0]] = wagon[1]

    # Finner stasjoner mellom start- og slutt:
    stations_in_between = route_stations_in_between_dict[int(routenr)]
    stations_in_between.reverse()
    between_length = len(stations_in_between)
    sub_routes = []

    # Legger til alle delstrekninger på valgt strekning i en liste:
    if between_length != 0:
        sub_routes.append([start_station, stations_in_between[0]])
        for i in range(1, between_length):
            if (between_length > 1):
                sub_routes.append([stations_in_between[i-1], stations_in_between[i]])
        sub_routes.append([stations_in_between[between_length-1], end_station])
    else:
        sub_routes.append([start_station, end_station])

    
    wagon_available_seats_dict = {}
    for wagon in wagons:
        id = wagon[0]
        sub_routes_seats_dict = {}
        cursor.execute("SELECT plassnr FROM Plass WHERE vognID = ?", (str(id),))
        seats = [seat[0] for seat in cursor.fetchall()]
        for sub_route in sub_routes:
            start_sub_station = sub_route[0]
            end_sub_station = sub_route[1]

            sub_route_index = (start_sub_station, end_sub_station)

            avaliable_seats = []
            # Finner plasser i vognen:
            for seat in seats:
                # cursor.execute("SELECT * FROM Billett JOIN Kundeordre USING (ordrenr) WHERE vognID = ? AND plassnr = ? AND startstasjon = ? AND endestasjon = ? AND forekomstDato = ?", (str(id), str(seat), start_sub_station, end_sub_station, date.strftime("%Y-%d-%m")))
                cursor.execute("SELECT billettnr FROM Billett JOIN Kundeordre USING (ordrenr) WHERE vognID = ? AND plassnr = ? AND startstasjon = ? AND endestasjon = ? AND forekomstDato = ?", (str(id), str(seat), start_sub_station, end_sub_station, date.strftime("%Y-%d-%m")))
                ticket_count = cursor.fetchall()
                if (len(ticket_count) == 0):
                    avaliable_seats.append(seat)
                # cursor.execute("SELECT billettnr FROM Billett JOIN Kundeordre USING (ordrenr) WHERE vognID = ? AND plassnr = ? AND startstasjon = ? AND endestasjon = ? AND forekomstDato = ?", (str(id), str(seat), start_sub_station, end_sub_station, date))
            
            sub_routes_seats_dict[sub_route_index] = avaliable_seats
        
        unavailable_seats = []
        for seat in seats:
            for sub_route in [(sub_route[0], sub_route[1]) for sub_route in sub_routes]:
                available_seats_on_subroute = sub_routes_seats_dict[sub_route]
                if seat not in available_seats_on_subroute and seat not in unavailable_seats:
                    unavailable_seats.append(seat)

        print("----")
        print(unavailable_seats)
        print("----")

        available_seats = seats[:]
        for unavailable_seat in unavailable_seats:
            available_seats.remove(unavailable_seat)
        if (len(available_seats) != 0):
            wagon_available_seats_dict[id] = available_seats
    print(wagon_available_seats_dict)



    # Finner gyldige IDer for vognene i ruten:
    valid_ids = []
    print("\n")
    print("Tilgjengelige vogner på ruten:")
    for wagon in wagon_available_seats_dict.keys():
        valid_ids.append(wagon)
        print(f"ID: {wagon}, Type: {wagon_types[wagon]}")

    
    print("\n")
    # Spør bruker om å oppgi én vogn til billettbestilling:
    print("""Velg vognene du ønsker å kjøpe plasser i. For å velge en vogn, skriv vognID-en i input-feltet og trykk 'Enter'. 
Dersom du ikke ønsker å velge flere vogner, skriv 'Stopp' i input-feltet.""")
    chosen_wagons = []
    chosen_ID = ""

    wagon_place_dict = {}
    
    finish = False
    while not finish:
        chosen_ID = input("Skriv inn vognID: ")
        if (chosen_ID.lower() == "stopp"):
            finish = True
            break
        while chosen_ID not in [str(id) for id in valid_ids]:
            print("Ugyldig vognID!")
            chosen_ID = input("Skriv inn vognID: ")
            if (chosen_ID.lower() == "stopp"):
                finish = True
                break
        if finish:
            break
        if int(chosen_ID) not in chosen_wagons:
            print("Du har valgt vogn med ID " + chosen_ID)
            chosen_wagons.append(int(chosen_ID))
            wagon_place_dict[int(chosen_ID)] = []
        else:
            print("Du har allerede valgt den vognen!")

    for wagon in chosen_wagons:
        places = wagon_available_seats_dict[wagon]

        valid_places = []
        print("Tilgjengelige plasser i vognen:", end= " ")
        for place in places:
            valid_places.append(place)
            print(place, end="")
            if (places.index(place) != len(places) - 1):
                print(",", end=" ")
            
        
        print("\n")
        print("""Velg plassene du ønsker å kjøpe billetter for. For å velge en plass, skriv plassnummeret i input-feltet og trykk 'Enter'. 
    Dersom du ikke ønsker å velge flere plasser, skriv 'Stopp' i input-feltet.""")
        chosen_places = []
        chosen_place = ""

        finish = False
        while not finish:
            chosen_place = input(f"Skriv inn plassnummer for vogn med ID {wagon}: ")
            if (chosen_place.lower() == "stopp"):
                finish = True
                break
            while chosen_place not in [str(place) for place in valid_places]:
                print("Ugyldig plassnummer!")
                chosen_place = input(f"Skriv inn plassnummer for vogn med ID {wagon}: ")
                if (chosen_place.lower() == "stopp"):
                    finish = True
                    break
            if finish:
                break
            if int(chosen_place) not in chosen_places:
                print(f"Du har valgt plass med nummer {chosen_place} i vogn med ID {wagon}")
                chosen_places.append(int(chosen_place))
                wagon_place_dict[wagon].append(int(chosen_place))
            else:
                print("Du har allerede valgt den plassen!")
    print(wagon_place_dict)

    def get_ticket_count(wagon_place_dict):
        ticket_count = 0
        for key in wagon_place_dict.keys():
            for value in wagon_place_dict[key]:
                ticket_count += 1
        return ticket_count

    #cursor.execute("SELECT billettnr FROM Billett WHERE vognID = ? AND vognID = ?", (chosen_ID,))
    #places = cursor.fetchall()
    #print(places)


    # Registrerer en ny kundeordre for bestillingen:
    new_orderno = get_next_orderno()
    cursor.execute("""INSERT INTO Kundeordre (ordrenr, dato, tid, antall, kundenr, forekomstDato, rutenr) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""", (get_next_orderno(), datetime.date.today(), datetime.datetime.now().strftime("%Y-%d-%m"), get_ticket_count(wagon_place_dict), customer_no, date.strftime("%Y-%d-%m"), routenr))
    con.commit()
    
    ## Hvis det finnes mellomstasjoner mellom start- og endestasjon, kjøp alle billettene:

    # Oppretter en billett for hver delstrekning på valgt strekning:
    for array in sub_routes:
        for wagon in wagon_place_dict.keys():
            for place in wagon_place_dict[wagon]:
                cursor.execute("""INSERT INTO Billett (billettnr, plassnr, vognID, ordrenr, startstasjon, endestasjon) 
                    VALUES (?, ?, ?, ?, ?, ?)""", (get_next_ticketno(), place, wagon, new_orderno, array[0], array[1]))
        con.commit()
    ##
    
    # Antar ingen billetter har blitt kjøpt:
    # Velger en eller flere plasser, inserter i billett-tabell plassnr, vognnr, dato og oppretter kundeordre

    # Sjekker om billett kjøpt:
    # Itererer gjennom billett-tabell på plassnr, vognnr og dato: hvis søk returnerer NULL => ledig
    # ellers: KJØPT 


    # 1. Billetkjøp - unik id, sette inn verdier fra bruker (husk validering)
    # 2. Billetkjøp - bare vis vogner med ledige plasser
    # 3  Delstrekninger - kjøpe alle billetter mellom start- og endestasjon hvis ledig
    # 4. Brukervennlighet ved inputs o.l.