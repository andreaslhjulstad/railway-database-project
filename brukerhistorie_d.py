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
        start_station = input("Skriv inn en startstasjon: ").lower().title()

    end_station = input(
        "Skriv inn en endestasjon (må være forskjellig fra startstasjon): ").lower().title()

    while not end_station in saved_stations or end_station == start_station:
        end_station = input(
            "Skriv inn en endestasjon (må være forskjellig fra startstasjon): ").lower().title()

    datestr = input("Skriv inn en dato på formatet 'YYYY-DD-MM': ")
    while not date_valid(datestr):
        datestr = input("Skriv inn en dato på format 'YYYY-DD-MM': ")
    (year, day, month) = datestr.split('-')
    year = int(year)
    month = int(month)
    day = int(day)
    date = datetime.date(year, month, day)

    timestr = input("Skriv inn et klokkelsett på formatet 'HH:MM': ")
    while not time_valid(timestr):
        timestr = input("Skriv inn et klokkelsett på formatet 'HH:MM': ")
    (hours, minutes) = timestr.split(":")
    hours = int(hours)
    minutes = int(minutes)
    time = datetime.time(hours, minutes)

    return (start_station, end_station, date, time)


# Validering for dato
def date_valid(datestr):
    try:
        (year, day, month) = datestr.split('-')
    except ValueError:
        return False

    validformat = re.fullmatch('[0-9]{4}-[0-9]{2}-[0-9]{2}', datestr)
    if not validformat:
        return False

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

    today = datetime.date.today().strftime("%Y-%d-%m")
    date = datetime.date(year, month, day).strftime("%Y-%d-%m")

    if date < today:
        return False

    return True


# Validering for tidspunkt
def time_valid(timestr):
    try:
        (hours, minutes) = timestr.split(':')
    except ValueError:
        return False

    validformat = re.fullmatch('[0-9]{2}:[0-9]{2}', timestr)
    if not validformat:
        return False

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


# Returnerer en oversikt over tidspunkt et tog er innom enten startstasjonen eller endestasjonen på datoens ukedag eller neste
def get_timetable(start_station, end_station, curr_weekday, next_weekday):
    cursor.execute("SELECT * FROM Togrutetabell WHERE (stasjon = ? OR stasjon = ?) AND (rutenr IN (SELECT rutenr From Driftsdager WHERE (ukedag = ? OR ukedag = ?)))",
                   (start_station, end_station, curr_weekday, next_weekday))
    timetable = cursor.fetchall()
    return timetable


# Henter ut ruter som går fra startstasjonen til endestasjonen på brukerens gitte ukedag
def get_valid_routes(timetable, start_station, end_station):
    start_station_times = []
    end_station_times = []

    for row in timetable:
        routeno = int(row[0])

        station = row[1]
        arrival_timestr = row[2]
        departing_timestr = row[3]

        if station == start_station:
            start_station_times.append(
                (routeno, arrival_timestr, departing_timestr))
        elif station == end_station:
            end_station_times.append(
                (routeno, arrival_timestr, departing_timestr))

    valid_routes = []
    for start_station_time in start_station_times:
        start_station_routeno = start_station_time[0]
        departing_timestr = start_station_time[2]

        if departing_timestr is not None:
            start_departing_times = departing_timestr.split(":")
            start_departing_hours = int(start_departing_times[0])
            start_departing_minutes = int(start_departing_times[1])
            start_departing_time = datetime.time(
                start_departing_hours, start_departing_minutes)
        else:
            start_departing_time = None

        for end_station_time in end_station_times:
            end_station_routeno = end_station_time[0]
            arrival_timestr = end_station_time[1]

            if arrival_timestr is not None:
                end_arrival_times = arrival_timestr.split(":")
                end_arrival_hours = int(end_arrival_times[0])
                end_arrival_minutes = int(end_arrival_times[1])
                end_arrival_time = datetime.time(
                    end_arrival_hours, end_arrival_minutes)
            else:
                end_arrival_time = None

            if end_station_routeno == start_station_routeno:
                if end_arrival_time is not None and start_departing_time is not None:
                    # TODO: fiks håndtering av tidspunkt (nattog som begynner før 00:00 skal også legges til)
                    if end_arrival_time > start_departing_time:
                        valid_routes.append(
                            (start_station_routeno, start_departing_time))
    return valid_routes


# Henter ut det endelige resultatet av togruter som går fra startstasjonen til endestasjonen med en forekomst på den gitte datoen
def get_final_result(valid_routes, occurence_rows, datestr, next_datestr, time):
    final_result = []
    for route in valid_routes:
        for row in occurence_rows:
            if route[0] == row[1] and (datestr == row[0] or next_datestr == row[0]):
                if (datestr == row[0] and route[1] < time):
                    continue
                final_result.append(route + (row[0],))

    sorted_final_result = sorted(final_result, key=lambda x: x[1])
    return sorted_final_result


# Henter ut alle togruteforekomster
def get_occurence_rows():
    cursor.execute("SELECT * FROM Togruteforekomst")
    occurence_rows = cursor.fetchall()
    return occurence_rows


def main():
    print("-------------------------------Finn togruter-------------------------------")
    print("\n")
    (start_station, end_station, date, time) = get_user_input()
    (curr_weekday, next_weekday) = get_weekdays(date)

    next_datestr = (date + datetime.timedelta(1)).strftime("%Y-%d-%m")
    datestr = date.strftime("%Y-%d-%m")
    timestr = time.strftime("%H:%M")

    timetable = get_timetable(
        start_station, end_station, curr_weekday, next_weekday)
    valid_routes = get_valid_routes(timetable, start_station, end_station)
    occurrence_rows = get_occurence_rows()
    final_result = get_final_result(
        valid_routes, occurrence_rows, datestr, next_datestr, time)

    print("\n")
    print(
        f"Disse rutene går fra {start_station} til {end_station} etter klokka {timestr} den {datestr} eller neste dag:")
    for result in final_result:
        print(
            f"Rutenr: {result[0]}, Tidspunkt: {result[1]}, Dato: {result[2]}")
    print("\n")
    print("---------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
