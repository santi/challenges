__author__ = "Santi"

"""
Et barn løper opp en trapp med 30 trinn, og kan ta enten ett, to eller tre steg omgangen.
Hvor mange ulike måter kan barnet løpe opp trappen?
"""


def stairs(n):
    fib = [1, 2, 4]
    for i in range(3, n):
        fib.append(fib[i - 1] + fib[i - 2] + fib[i - 3])
    return fib[-1]


print(stairs(30))