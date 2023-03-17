""" Bruker skal kunne søke etter togruter som går mellom en startstasjon og en sluttstasjon, med
utgangspunkt i en dato og et klokkeslett. Alle ruter den samme dagen og den neste skal
returneres, sortert på tid. Denne funksjonaliteten skal programmeres. """

import sqlite3
import re
import datetime

# Opprett tilkobling til databasen
con = sqlite3.connect("jernbaneDatabase.db")
cursor = con.cursor()

# Henter lagrede jernbanestasjoner (for validering)
cursor.execute("SELECT navn FROM Jernbanestasjon")
rows = cursor.fetchall()
saved_stations = []
for row in rows:
    saved_stations.append(row[0])


# Ber brukeren om å skrive inn startstasjon, endestasjon dato og tidspunkt, validerer disse og lagrer dem dersom de er gyldige
def get_user_input():
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

    datestr = input("Skriv inn en dato på formatet 'YYYY-DD-MM': ")
    while not date_valid(datestr):
        print("Ugyldig dato! Datoen må være på riktig format og i fremtiden (eller i dag)")
        datestr = input("Skriv inn en dato på formatet 'YYYY-DD-MM': ")
    (year, day, month) = datestr.split('-')
    year = int(year)
    month = int(month)
    day = int(day)
    date = datetime.date(year, month, day)

    timestr = input("Skriv inn et klokkelsett på formatet 'HH:MM': ")
    while not time_valid(timestr):
        print("Ugyldig klokkeslett! Klokkeslettet må være på riktig format")
        timestr = input("Skriv inn et klokkelsett på formatet 'HH:MM': ")
    (hours, minutes) = timestr.split(":")
    hours = int(hours)
    minutes = int(minutes)
    time = datetime.time(hours, minutes)

    return (start_station, end_station, date, time)


# Validering for dato
def date_valid(datestr):
    validformat = re.fullmatch('[0-9]{4}-[0-9]{2}-[0-9]{2}', datestr)
    if not validformat:
        return False

    (year, day, month) = datestr.split('-')

    year = int(year)
    month = int(month)
    day = int(day)
    if year < 0 or month < 0 or day < 0:
        return False
    elif month > 12 or day > 31:
        return False
    elif day > 30 and month in [4, 6, 9, 11]:
        return False
    elif (day > 29 and month == 2) or (day > 28 and month == 2 and year % 4 != 0):
        return False

    today = datetime.date.today()
    date = datetime.date(year, month, day)

    if date < today:
        return False

    return True


# Validering for tidspunkt
def time_valid(timestr):
    validformat = re.fullmatch('[0-9]{2}:[0-9]{2}', timestr)
    if not validformat:
        return False

    (hours, minutes) = timestr.split(':')

    hours = int(hours)
    minutes = int(minutes)
    if hours < 0 or minutes < 0:
        return False
    elif hours > 23 or minutes > 59:
        return False

    return True


# Returnerer ukedag for datoen brukeren skrev inn, samt neste ukedag
def get_weekdays(date):
    weekday_int = date.weekday()

    match weekday_int:
        case 0:
            curr_weekday = "mandag"
            next_weekday = "tirsdag"
        case 1:
            curr_weekday = "tirsdag"
            next_weekday = "onsdag"
        case 2:
            curr_weekday = "onsdag"
            next_weekday = "torsdag"
        case 3:
            curr_weekday = "torsdag"
            next_weekday = "fredag"
        case 4:
            curr_weekday = "fredag"
            next_weekday = "lørdag"
        case 5:
            curr_weekday = "lørdag"
            next_weekday = "søndag"
        case 6:
            curr_weekday = "søndag"
            next_weekday = "mandag"

    return (curr_weekday, next_weekday)


# Returnerer en oversikt over tidspunkt et tog er innom en stasjon på de gitte ukedagene
def get_station_rows(station, curr_weekday, next_weekday):
    cursor.execute("SELECT * FROM Togrutetabell WHERE stasjon = ? AND (rutenr IN (SELECT rutenr From Driftsdager WHERE (ukedag = ? OR ukedag = ?)))",
                   (station, curr_weekday, next_weekday))
    return cursor.fetchall()


# Henter ut ruter som går fra startstasjonen til endestasjonen på brukerens gitte ukedag
def get_valid_routes(start_station_rows, end_station_rows):
    valid_routes = []
    for start_station_row in start_station_rows:
        start_station_routeno = start_station_row[0]
        start_station_stationno = start_station_row[4]

        for end_station_row in end_station_rows:
            end_station_routeno = end_station_row[0]
            end_station_stationno = end_station_row[4]

            if (start_station_routeno == end_station_routeno) and (start_station_stationno < end_station_stationno):
                start_departing_time = start_station_row[3]
                if start_departing_time is not None:
                    start_departing_times = start_departing_time.split(":")
                    start_departing_hours = int(start_departing_times[0])
                    start_departing_minutes = int(start_departing_times[1])
                    start_departing_time = datetime.time(
                        start_departing_hours, start_departing_minutes)
                    valid_routes.append(
                        (start_station_routeno, start_departing_time))

    return valid_routes


# Henter ut alle togruteforekomster
def get_occurence_rows():
    cursor.execute("SELECT * FROM Togruteforekomst")
    occurence_rows = cursor.fetchall()
    return occurence_rows


# Henter ut det endelige resultatet av togruter som går fra startstasjonen til endestasjonen med en forekomst på den gitte datoen
def get_final_result(valid_routes, occurence_rows, date, next_date, time):
    datestr = date.strftime("%Y-%d-%m")
    next_datestr = next_date.strftime("%Y-%d-%m")
    
    final_result = []
    for route in valid_routes:
        for row in occurence_rows:
            if row[1] == route[0] and (row[0] == datestr or row[0] == next_datestr):
                # Togruten går samme dag og før brukerens valgte tidspunkt
                if row[0] == datestr and route[1] < time:
                    continue
                if row[0] == datestr:
                    result_date = date
                elif row[0] == next_datestr:
                    result_date = next_date
                final_result.append((route[0], result_date, route[1]))

    # Sorterer først på dato, deretter på tidspunkt
    sorted_final_result = sorted(final_result, key=lambda x: (x[1], x[2]))
    return sorted_final_result


def main():
    print("------------------------------------------------Finn togruter-------------------------------------------------")
    print("\n")

    print("Tilgjengelige stasjoner:")
    for station in saved_stations:
        print(station)
    print("\n")

    (start_station, end_station, date, time) = get_user_input()
    next_date = date + datetime.timedelta(1)
    (curr_weekday, next_weekday) = get_weekdays(date)

    # Formatering for print output
    datestr = date.strftime("%Y-%d-%m")
    next_datestr = next_date.strftime("%Y-%d-%m")
    timestr = time.strftime("%H:%M")

    start_station_rows = get_station_rows(
        start_station, curr_weekday, next_weekday)
    end_station_rows = get_station_rows(
        end_station, curr_weekday, next_weekday)

    valid_routes = get_valid_routes(start_station_rows, end_station_rows)
    occurrence_rows = get_occurence_rows()
    final_result = get_final_result(
        valid_routes, occurrence_rows, date, next_date, time)

    print("\n")
    if (len(final_result) > 0):
        print(
            f"Disse rutene går fra {start_station} til {end_station} etter klokka {timestr} den {datestr} eller {next_datestr}:")
        for result in final_result:
            routeno = result[0]
            timestamp_formatted = result[2].strftime("%H:%M")
            date_formatted = result[1].strftime("%Y-%d-%m")
            print(
                f"Rutenr: {routeno}, Tidspunkt: {timestamp_formatted}, Dato: {date_formatted}")
    else:
        print(
            f"Det går dessverre ingen ruter fra {start_station} til {end_station} etter klokka {timestr} den {datestr} eller {next_datestr}")
    print("\n")
    print("--------------------------------------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()

# Lukker tilkobling til databasen
con.close()
