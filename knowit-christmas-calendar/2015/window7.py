__author__ = 'vemund'
c = 0
for i in range(1001):
    if i % 7 == 0 and int("".join(reversed(list(str(i))))) % 7 == 0:
        c += i
print c
