__author__ = 'vemund'

import math
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.ceil(math.sqrt(n))), 2):
        if n % i == 0:
            return False
    return True

c = 0
for i in range(1001):
    if is_prime(i) and is_prime(int("".join(reversed(list(str(i)))))) and i != int("".join(reversed(list(str(i))))):
        c += 1
print c
