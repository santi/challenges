__author__ = 'vemund'

n = "12345678987654321"
digits = len(n) - 1
count = 0

for i in range(digits, 0, -1):
    count += int(n[digits - i]) * i*(10**(i - 1))
    if int(n[digits - i]) == 2:
        try:
            count += int(n[digits - i + 1:]) + 1
        except ValueError:
            count += 1
    elif int(n[digits - i]) > 2:
        count += 10**i
print count



