__author__ = 'Vemund'

import math

def checkPrime(tall):
    if tall == 2:
        return True
    for i in range(2,tall):
        if tall%i == 0:
            return False
    return True




mirptall = 0
for i in range(2,1001):
    tekstTall = str(i)
    liste = []
    for char in tekstTall:
        liste.append(char)
    liste.reverse()
    tekstTall = ""
    for nummer in liste:
        tekstTall = tekstTall+nummer
    tekstTall = int(tekstTall)
    if checkPrime(i) and checkPrime(tekstTall) and i != tekstTall:
        mirptall += 1
        print(i,"og",tekstTall,"er mirptall!")
print(mirptall)
