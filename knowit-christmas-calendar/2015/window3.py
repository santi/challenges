# coding=utf-8
__author__ = 'vemund'

"""
Programmererenes dag feires hvert år på den 256. dagen (eller 2^8. dagen om du vil) i året.
Hvor mange ganger fra og med år 1 til og med år 2015 har dette forekommet på en fredag om
en antar at 1. januar år 1 var en fredag i, samt at dagens skuddårsregler og kalendersystem har
vært gjeldende i hele perioden?

Hint: Skuddår er forøvrig et år som er delelig på 4 og ikke 100 med mindre det er delelig på 400

OBS: Er blitt gjort oppmerksom på et avvik i oppgaven. Svaret som er lagt inn på oppgaven later
til å anta at den første dagen i året er den "nulte" dagen i året.
"""

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

friday = 4
fridays = 0
day = 4
for year in range(1, 2016):
    if (day + 256) % 7 == 4:
        fridays += 1
    if is_leap_year(year):
        day = (day + 366) % 7
    else:
        day = (day + 365) % 7
print fridays

