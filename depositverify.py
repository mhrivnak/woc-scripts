#!/usr/bin/env python3

# From myfbo, find the two database-generated reports with names "mhrivnak -
# deposits" and "mhrivnak - flights". Run them and save their contents as CSV
# files named "deposits.csv" and "flights.csv" respectively, in the same
# directory as this file. Then run this file.

import csv

FIRSTNAME = 'First Name'
LASTNAME = 'Last Name'
CUSTOMERID = 'Customer ID'
SPECIALBALANCE = 'Special Balance'
DESCRIPTION = 'Description'
DISPATCHDATE = 'Dispatch Date'
INACTIVE = 'Inactive?'
MAINTENANCE = 'Maintenance'

C172 = 'C172S'
C152 = 'C152'
PA28 = 'PA28'
M20J = 'M20J'


def main():
    deposits = {}

    with open('deposits.csv') as depositscsv:
        depositreader = csv.DictReader(depositscsv)
        for row in depositreader:
            # if they resigned, not much we can do now
            if row[INACTIVE] == 'True':
                deposits[row[CUSTOMERID]] = 1000000
            # ignore MX flights by assuming a large deposit
            elif row[FIRSTNAME] == MAINTENANCE:
                deposits[row[CUSTOMERID]] = 1000000
            else:
                deposits[row[CUSTOMERID]] = float(row[SPECIALBALANCE])
                

    with open('flights.csv') as flightscsv:
        flightreader = csv.DictReader(flightscsv)
        for row in flightreader:
            balance = deposits.get(row[CUSTOMERID], 0)
            ptype = row[DESCRIPTION]

            if ptype == C152 and balance < 300:
                snitch(balance, row)
            if ptype == PA28 and balance < 600:
                snitch(balance, row)
            if ptype == C172 and balance < 900:
                snitch(balance, row)
            if ptype == M20J and balance < 1200:
                snitch(balance, row)


def snitch(balance, row):
    print("Balance {} insufficient for {}. {} {} on {}".format(balance, row[DESCRIPTION], row[FIRSTNAME], row[LASTNAME], row[DISPATCHDATE]))


if __name__ == "__main__":
    main()
