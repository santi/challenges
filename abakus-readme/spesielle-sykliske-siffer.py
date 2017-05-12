#!/usr/bin/env python
from math import sqrt, ceil
"""
Assignment: What is the sum of all cyclic prime numbers between 0 and 1000000?
https://en.wikipedia.org/wiki/Circular_prime
"""


def generate_primes(limit):
    """Generate prime numbers.

    Uses the Sieve of Erasthenes algorithm to generate
    all primes up to and including limit
    """
    numbers = [_ for _ in range(2, limit + 1)]

    for i in range(ceil(sqrt(len(numbers)))):
        if numbers[i]:
            for multiple in range(2 * numbers[i], len(numbers) + 2, numbers[i]):
                numbers[multiple - 2] = False
    return [x for x in numbers if x]


def cycle_digit(number):
    return number[-1] + number[:-1]


def find_cyclic_primes(numbers):
    cyclic_numbers = []
    numbers_dict = dict([(str(number), True) for number in numbers])
    for number in numbers:
        current_number = str(number)
        cyclic = True
        for _ in range(len(current_number)):
            if not numbers_dict.get(current_number, False):
                cyclic = False
                break
            current_number = cycle_digit(current_number)
        if cyclic:
            cyclic_numbers.append(number)
    return cyclic_numbers


print(sum(find_cyclic_primes(generate_primes(1000000))))
