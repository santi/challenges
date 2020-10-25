from sys import stdin
from math import floor, sqrt


n = int(stdin.readline())

def get_num_factors(n):
    factors = 0
    candidate = 2
    while candidate * candidate <= n:
        if n % candidate == 0:
            n //= candidate
            factors += 1
        else:
            candidate += 1
    return factors + 1

answer = get_num_factors(n)
print(answer)