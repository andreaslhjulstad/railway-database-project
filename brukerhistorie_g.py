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


# Henter inn brukerens kundenr vha. e-postadressen som en slags primitiv form for innlogging
def get_customerno():
    # Henter registrerte e-postadresser
    cursor.execute("SELECT epost FROM Kunde")
    saved_emails = cursor.fetchall()
    if not len(saved_emails) == 0: 
        # Henter inn e-postadresse fra bruker
        email = input("Skriv inn e-posten din: ")
        while not email in saved_emails[0]:
            print("Den e-postadressen finnes ikke i registeret!")
            email = input("Skriv inn e-posten din: ")

        # Finner kundenummer til bruker gitt email
        cursor.execute("SELECT kundenr FROM Kunde WHERE epost = ?", (email,))
        customerno = cursor.fetchall()[0][0]
        return customerno
    else:
        return 0


# Henter inn start- og endestasjon fra brukerinput, og sjekker at de er gyldige
def get_stations():
    print("\n")
    start_station = input("Skriv inn en startstasjon: ").lower().title()
    while not start_station in saved_stations:
        print("Den stasjonen finnes ikke!")
        start_station = input("Skriv inn en startstasjon: ").lower().title()

    end_station = input(
        "Skriv inn en endestasjon: ").lower().title()
    while not end_station in saved_stations:
        print("Den stasjonen finnes ikke!")
        end_station = input(
            "Skriv inn en endestasjon: ").lower().title()

    while end_station == start_station:
        print("Endestasjon må være forskjellig fra startstasjon!")
        end_station = input(
            "Skriv inn en endestasjon: ").lower().title()

    return (start_station, end_station)


# Returnerer True dersom ruten kjører hovedretningen til banestrekningen, ellers False
def is_main_direction(routeno):
    cursor.execute(
        "SELECT DISTINCT kjørerHovedretning FROM DelstrekningPåRute WHERE rutenr = ?", (routeno,))
    rows = cursor.fetchall()
    main_direction = rows[0][0]
    if (main_direction == "true"):
        return True
    return False


# Henter neste billettnr ved å sjekke billettnr som sist ble lagret i databasen og legg til 1
def get_next_ticketno():
    cursor.execute("SELECT billettnr FROM Billett")
    rows = cursor.fetchall()

    max_ticketno = 0
    for row in rows:
        if row[0] > max_ticketno:
            max_ticketno = row[0]
    return max_ticketno + 1


# Henter neste ordrenr ved å sjekke ordrenr som sist ble lagret i databasen og legg til 1
def get_next_orderno():
    cursor.execute("SELECT ordrenr FROM Kundeordre")
    rows = cursor.fetchall()

    max_orderno = 0
    for row in rows:
        if row[0] > max_orderno:
            max_orderno = row[0]
    return max_orderno + 1


# Regner ut antall billetter
def get_ticket_count(wagon_spot_dict):
    ticket_count = 0
    for key in wagon_spot_dict.keys():
        for value in wagon_spot_dict[key]:
            ticket_count += 1
    return ticket_count


# Henter alle togrutenummer
def get_all_routenos():
    cursor.execute("SELECT rutenr FROM Togrute")
    route_numbers = cursor.fetchall()
    return route_numbers


# Henter mulige vogner for togruten
def get_all_wagons(routeno):
    cursor.execute(
        "SELECT vognID FROM Togrute JOIN VognIOppsett USING (oppsettID) JOIN Vogn USING (vognID) WHERE rutenr = ?", (routeno,))
    wagons = cursor.fetchall()
    return wagons


def get_sleeping_wagon_arrangement(wagon_id):
    cursor.execute("SELECT antallSoveKupeer, sengerPrKupe FROM Sovevogn WHERE vognID = ?", (wagon_id,))
    arrangement = cursor.fetchall()[0]
    return arrangement


# Henter oppsettID-en til en oppgitt rute
def get_wagon_layout(routeno):
    cursor.execute("SELECT oppsettID FROM Togrute WHERE rutenr = ?", (routeno,))
    wagon_layout = cursor.fetchall()[0][0]
    return wagon_layout


def get_available_spots_in_wagons(wagons, sub_routes, chosen_date, routeno):
    sub_routes_taken_spots_dict = {}
    for sub_route in sub_routes:
        start_sub_station = sub_route[0]
        end_sub_station = sub_route[1]
        
        layout_ID = get_wagon_layout(routeno)
        
        # Finner plasser i vognen som er bestilt på delstrekningen på kundens valgte dato
        cursor.execute("""SELECT Billett.vognID, plassnr FROM Billett JOIN Kundeordre USING (ordrenr) JOIN VognIOppsett USING (vognID) 
                        WHERE startstasjon = ? AND endestasjon = ? AND forekomstDato = ? AND oppsettID = ?
                        ORDER BY Billett.vognID""",
                        (start_sub_station, end_sub_station, chosen_date.strftime("%Y-%d-%m"), layout_ID))
        rows = cursor.fetchall()
        
        wagon_unavailable_spots_dict = {}
        for row in rows:
            if row[0] in wagon_unavailable_spots_dict.keys():
                wagon_unavailable_spots_dict[row[0]].append(row[1])
            else:
                wagon_unavailable_spots_dict[row[0]] = [row[1]]

        sub_routes_taken_spots_dict[sub_route] = wagon_unavailable_spots_dict

    wagon_available_spots_dict = {}
    for wagon in wagons:
        id = wagon[0]
        type = get_wagon_type(id)
        unavailable_spots = set()
        cursor.execute(
            "SELECT plassnr FROM Plass WHERE vognID = ?", (id,))
        spots = {spot[0] for spot in cursor.fetchall()}
        for spot in spots:
            for sub_route in sub_routes_taken_spots_dict.keys():
                taken_spots_dict = sub_routes_taken_spots_dict[sub_route]
                if id in taken_spots_dict.keys():
                    if spot in taken_spots_dict[id]:
                        # Dersom det er en sovevogn, legg alle senger i samme sovekupé til i liste over opptatte plasser
                        if (type == 'Sovevogn'):
                            compartments, beds_per_compartment = get_sleeping_wagon_arrangement(id)
                            position_in_compartment = spot % beds_per_compartment
                        
                            # Modulo-aritmetikk gir at vognen på "siste plass i kupeen" er lik 0, vi vil ha den lik antallet senger i stedet
                            if position_in_compartment == 0:
                                position_in_compartment = beds_per_compartment

                            diff_top = beds_per_compartment - position_in_compartment
                            diff_bottom = position_in_compartment - 1
                            for i in range(1, diff_top + 1):
                                unavailable_spots.add(spot + i)
                            for j in range(1, diff_bottom + 1):
                                unavailable_spots.add(spot - j)
                        unavailable_spots.add(spot)

        available_spots = list(spots - unavailable_spots)
        available_spots.sort()
        if len(available_spots) > 0:
            wagon_available_spots_dict[id] = available_spots

    """
    Liten forklaring for hva vi har tenkt her:
    Vi ønsker å bare vise vogner som har ledige plasser på hele ruten brukeren har valgt. 
    Vi henter derfor, for hver delstrekning, inn de plassene som er opptatt på den delstrekningen på brukerens valgte dato.
    Deretter sjekker vi for hver mulige plass i hver vogn, om denne plassen er utilgengelig på noen av delstrekningene. Dersom det er det,
    legg den til i en mengde med utilgjengelige plasser. For sovevogner står det spesifisert i oppgaven at en ikke skal kunne booke en seng i en kupé
    der noen andre allerede har booket en seng, derfor legges alle sengene i en sovekupé til i listen over utilgjengelige plasser dersom en av dem er booket.
    De plassene som er tilgjengelige under hele ruten i en vogn er da differansen mellom mengden 
    av alle mulige plasser i denne vognen og de plassene som er opptatt på minst én delstrekning i vognen. 
    """

    return wagon_available_spots_dict


def get_chosen_date(routeno):
    # Henter datoer for forekomster på den oppgitte togruta
    valid_dates = []
    cursor.execute(
        "SELECT dato FROM Togruteforekomst WHERE rutenr = ?", (routeno,))
    avaliable_dates = cursor.fetchall()
    # Hvis det ikke finnes noen forekomster, informer bruker
    if (len(avaliable_dates) == 0):
        print("Det er dessverre ingen registrerte forekomster av den oppgitte togruten for øyeblikket. Prøv igjen senere.")
        return None
    else:
        date_today = datetime.date.today()
        for i in range(len(avaliable_dates)):
            date_element = str(avaliable_dates[i][0])
            year, day, month = date_element.split("-")
            date = datetime.date(int(year), int(month), int(day))
            if (date >= date_today):
                valid_dates.append(date.strftime("%Y-%d-%m"))

    # Hent ønsket dato fra bruker og sjekk at den er gyldig
    print("\n")
    print("Gyldige datoer for reisen:", end=" ")
    for valid_date in valid_dates:
        print(valid_date, end="")
        if (valid_dates.index(valid_date) != len(valid_dates) - 1):
            print(",", end=" ")
        else:
            print("")

    chosen_datestr = input(
        "Skriv inn datoen du vil reise på formatet 'YYYY-DD-MM': ")
    while not brukerhistorie_d.date_valid(chosen_datestr):
        print("Datoen du skrev inn er ikke gyldig!")
        chosen_datestr = input(
            "Skriv inn datoen du vil reise på formatet 'YYYY-DD-MM': ")

    while chosen_datestr not in valid_dates:
        print("Det går ingen forekomster av togruten du valgte på den datoen!")
        chosen_datestr = input(
            "Skriv inn datoen du vil reise på formatet 'YYYY-DD-MM': ")

    # Konverterer den valgte forekomstdatoen til gyldig format for databasen
    year, day, month = chosen_datestr.split("-")
    chosen_date = datetime.date(int(year), int(month), int(day))
    return chosen_date


# Henter ut vogntypen til vogn-iden som tas som argument
def get_wagon_type(wagon_id):
    cursor.execute("SELECT type FROM Vogn WHERE vognID = ?", (wagon_id,))
    wagon_type = cursor.fetchall()[0][0]
    return wagon_type


# Ber brukeren om å velge tilgjengelige vogner og plasser og lagrer disse i en dictionary
def get_chosen_wagons_and_spots(wagon_available_spots_dict):
    # Finner gyldige IDer for vognene i ruten
    valid_ids = []
    print("\n")
    if len(wagon_available_spots_dict.keys()) == 0:
        print("Denne togruten er dessverre utsolgt")
        return None
    print("Tilgjengelige vogner på ruten:")
    for wagon in wagon_available_spots_dict.keys():
        valid_ids.append(wagon)
        print(f"ID: {wagon}, Type: {get_wagon_type(wagon)}")

    print("\n")
    # Spør bruker om å oppgi én vogn til billettbestilling
    print("Velg vognene du ønsker å kjøpe plasser i. For å velge en vogn, skriv vognID-en i innskrivings-feltet og trykk 'Enter'.")
    print("Dersom du ikke ønsker å velge flere vogner, skriv 'Stopp' i innskrivings-feltet.")
    chosen_wagons = []
    chosen_ID = ""

    wagon_chosen_spots_dict = {}

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
            wagon_chosen_spots_dict[int(chosen_ID)] = []
        else:
            print("Du har allerede valgt den vognen!")

    for wagon in chosen_wagons:
        spots = wagon_available_spots_dict[wagon]

        valid_spots = []
        print("Tilgjengelige plasser i vognen:", end=" ")
        for spot in spots:
            valid_spots.append(spot)
            print(spot, end="")
            if (spots.index(spot) != len(spots) - 1):
                print(",", end=" ")

        print("\n")
        print("Velg plassene du ønsker å kjøpe billetter for. For å velge en plass, skriv plassnummeret i innskrivings-feltet og trykk 'Enter'.")
        print(
            "Dersom du ikke ønsker å velge flere plasser, skriv 'Stopp' i innskrivings-feltet.")
        chosen_spots = []
        chosen_spot = ""

        finish = False
        while not finish:
            chosen_spot = input(
                f"Skriv inn plassnummer for vogn med ID {wagon}: ")
            if (chosen_spot.lower() == "stopp"):
                finish = True
                break
            while chosen_spot not in [str(spot) for spot in valid_spots]:
                print("Ugyldig plassnummer!")
                chosen_spot = input(
                    f"Skriv inn plassnummer for vogn med ID {wagon}: ")
                if (chosen_spot.lower() == "stopp"):
                    finish = True
                    break
            if finish:
                break
            if int(chosen_spot) not in chosen_spots:
                print(
                    f"Du har valgt plass med nummer {chosen_spot} i vogn med ID {wagon}")
                chosen_spots.append(int(chosen_spot))
                wagon_chosen_spots_dict[wagon].append(int(chosen_spot))
            else:
                print("Du har allerede valgt den plassen!")

    chosen = False
    if len(wagon_chosen_spots_dict) > 0:
        for wagon in wagon_chosen_spots_dict.keys():
            if len(wagon_chosen_spots_dict[wagon]) > 0:
                chosen = True

    if not chosen:
        print("\n")
        print("Du har ikke valgt noen vogner eller plasser, bestillingen avbrytes")
        return None

    return wagon_chosen_spots_dict


# Registrerer en ny kundeordre for bestillingen
def place_order(customerno, ticket_count, chosen_date, routeno):
    orderno = get_next_orderno()
    cursor.execute("""INSERT INTO Kundeordre (ordrenr, dato, tid, antall, kundenr, forekomstDato, rutenr) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""", (orderno, datetime.date.today().strftime("%Y-%d-%m"), datetime.datetime.now().strftime("%H:%M:%S"), ticket_count, customerno, chosen_date.strftime("%Y-%d-%m"), routeno))
    con.commit()
    return orderno


# Oppretter en billett for hver valgte plass i de valgte vognene for hver delstrekning på valgt strekning
def create_tickets(orderno, sub_routes, wagon_chosen_spots_dict):
    for sub_route in sub_routes:
        for wagon in wagon_chosen_spots_dict.keys():
            for spot in wagon_chosen_spots_dict[wagon]:
                cursor.execute("""INSERT INTO Billett (billettnr, plassnr, vognID, ordrenr, startstasjon, endestasjon) 
                    VALUES (?, ?, ?, ?, ?, ?)""", (get_next_ticketno(), spot, wagon, orderno, sub_route[0], sub_route[1]))
        con.commit()


def main():
    print("----------------------------------------------------------Bestill togreise----------------------------------------------------------")

    print("\n")
    print("Tilgjengelige stasjoner:")
    for station in saved_stations:
        print(station)
    print("\n")

    customerno = get_customerno()
    if customerno != 0:
        start_station, end_station = get_stations()
        route_numbers = get_all_routenos()

        # Liste for togruter med oppgitt strekning, samt liste over alle stasjoner mellom start- og endestasjon
        train_routes = []
        stations_in_between = []
        route_stations_in_between_dict = {}

        # Itererer gjennom alle togruter
        for i in range(len(route_numbers)):
            # Henter alle stasjoner på ruten, samt deres stasjonsnr
            cursor.execute("SELECT * FROM Togrutetabell WHERE rutenr = ?",
                        (str(route_numbers[i][0]),))
            stationQuery = cursor.fetchall()

            stations = []
            stationno = []
            stations_dict = {}

            # Lager map mellom stasjoner og deres stasjonnr
            for row in stationQuery:
                stations.append(row[1])
                stationno.append(row[4])

            stations_dict = {stations[j]: stationno[j]
                            for j in range(len(stations))}

            # Sjekker om start- og endestasjonen er i togruten
            if ((start_station in stations) and (end_station in stations)):
                # Sjekker at endestasjon kommer etter startstasjon
                if stations_dict[end_station] > stations_dict[start_station]:
                    train_routes.append(route_numbers[i][0])

                    # Hvis det finnes mellomstasjoner på strekningen, legg dem til i en egen liste
                    for station in stations:
                        if ((stations_dict[station] > stations_dict[start_station]) and (stations_dict[station] < stations_dict[end_station])):
                            stations_in_between.append(station)

                    # Lager en mapping mellom hvert togrutenummer og tilhørende mellomstasjoner
                    route_stations_in_between_dict.update(
                        {route_numbers[i][0]:  stations_in_between})
                    # Tømmer mellomstasjoner før neste iterering
                    stations_in_between = []

        # Hvis ingen togruter inneholder oppgitt strekning, informer bruker
        available_routes = len(train_routes)
        if (available_routes == 0):
            print("Det finnes ingen registrert togrute for strekning " +
                start_station + " til " + end_station + "!")
        else:
            # Skriver ut hvilke togruter bruker kan velge mellom
            print("\n")
            print("Mulige togruter for strekning: ")
            for k in range(available_routes):
                print("Togrute nr. " + str(train_routes[k]))

            # Henter ønsket togrutenummer fra bruker
            routeno = input("Velg én togrute: ")
            while not routeno in [str(train_route) for train_route in train_routes]:
                routeno = input(
                    "Velg én togrute: ")
            print("Du har valgt togrute " + str(routeno))

            # Finner stasjoner mellom start- og slutt
            stations_in_between = route_stations_in_between_dict[int(routeno)]
            if (is_main_direction(routeno)):
                stations_in_between.reverse()
            between_length = len(stations_in_between)

            # Legger til alle delstrekninger på valgt strekning i en liste
            sub_routes = []
            if between_length != 0:
                sub_routes.append((start_station, stations_in_between[0]))
                for i in range(1, between_length):
                    if (between_length > 1):
                        sub_routes.append(
                            (stations_in_between[i-1], stations_in_between[i]))
                sub_routes.append(
                    (stations_in_between[between_length-1], end_station))
            else:
                sub_routes.append((start_station, end_station))

            chosen_date = get_chosen_date(routeno)
            if chosen_date is not None:
                wagons = get_all_wagons(routeno)
                wagon_available_spots_dict = get_available_spots_in_wagons(
                    wagons, sub_routes, chosen_date, routeno)
                wagon_chosen_spots_dict = get_chosen_wagons_and_spots(wagon_available_spots_dict)
                if wagon_chosen_spots_dict is not None:
                    ticket_count = get_ticket_count(wagon_chosen_spots_dict)
                    orderno = place_order(customerno, ticket_count, chosen_date, routeno)
                    create_tickets(orderno, sub_routes, wagon_chosen_spots_dict)

                    print("\n")
                    print("Din bestilling er nå lagt inn. God tur!")
    else:
        print("Det finnes ingen brukere i registeret!")
        print("Vennligst opprett en bruker for å bestille en togreise")
    print("\n")
    print("------------------------------------------------------------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()

# Lukker tilkobling til databasen
con.close()
