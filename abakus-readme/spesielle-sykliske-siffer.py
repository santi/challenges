#!/usr/bin/env python3
from math import sqrt, floor
"""
Assignment: What is the sum of all cyclic prime numbers between 0 and 1000000?
https://en.wikipedia.org/wiki/Circular_prime
"""


def generate_primes(limit):
    """Generate prime numbers.

    Uses the Sieve of Erasthenes algorithm to generate
    all primes up to and including limit.
    The time complexity of this algorithm is O(n log log n).
    """
    numbers = [_ for _ in range(2, limit + 1)]

    for i in range(floor(sqrt(len(numbers)))):
        if numbers[i]:
            for multiple in range(
                                numbers[i] * numbers[i],
                                len(numbers) + 2, numbers[i]
                                ):
                numbers[multiple - 2] = False
    return [x for x in numbers if x]


def cycle_digits(number):
    return number[-1] + number[:-1]


def find_cyclic_primes(primes):
    """Returns a list of all cyclic primes

    Given a list of prime numbers, this function tests if the prime
    is a cyclic prime by using a dictionary, and returns all cyclic primes
    """
    cyclic_primes = []
    primes_dict = dict([(str(number), True) for number in primes])
    for number in primes:
        current_number = str(number)
        cyclic = True
        for _ in range(len(current_number)):
            if not primes_dict.get(current_number, False):
                cyclic = False
                break
            current_number = cycle_digits(current_number)
        if cyclic:
            cyclic_primes.append(number)
    return cyclic_primes


print(sum(find_cyclic_primes(generate_primes(1000000))))
