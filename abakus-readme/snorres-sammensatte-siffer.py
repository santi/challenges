#!/usr/bin/env python3
"""
Assignment: What is the sum of the first 10 000 composite
numbers (not including 1)?
https://en.wikipedia.org/wiki/Composite_number
"""
import math as m


def is_composite(number):
    for i in range(2, int(m.sqrt(number)) + 1):
        if number % i == 0:
            return True
    return False


def get_n_first_composite_numbers(n):
    composite_numbers = []
    number = 4  # The first composite number
    while len(composite_numbers) < n:
        if is_composite(number):
            composite_numbers.append(number)
        number += 1
    return composite_numbers


print(sum(get_n_first_composite_numbers(10000)))
