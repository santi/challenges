#!/usr/bin/env python3
"""
Assignment: What is the sum of the three first Smith numbers,
that are also Fibonacci numbers? (Parie numbers)
https://en.wikipedia.org/wiki/Smith_number
"""


def fibonacci_generator():
    first = 0
    second = 1
    while True:
        temp = first + second
        first = second
        second = temp
        yield first


def get_sum_of_digits(number):
    digits = list(str(number))
    return sum(map(int, digits))


def is_smith_number(number):
    """
    A Smith number is a composite number where the sum of its digits are equal
    to the sum of the digits in the prime factors of the number
    """
    counter_digit_sum = get_sum_of_digits(number)
    prime_factors = fib_factors[number]

    if len(prime_factors) == 1:
        return False  # Must be a composite number

    prime_factor_digit_sum = sum(map(get_sum_of_digits, prime_factors))
    return counter_digit_sum == prime_factor_digit_sum


def flatten(array):
    new_array = []
    for element in array:
        if type(element) == list:
            for el in element:
                new_array.append(el)
        else:
            new_array.append(element)
    return new_array


def load_fib_factors():
    fib_factors = {}
    fib_gen = fibonacci_generator()

    fib = 0
    with open('fib_tables.txt') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].split('= ')
            lines[i][0] = fib
            lines[i][1] = lines[i][1].strip().split(' * ')

            for index, factor in enumerate(lines[i][1]):
                if '^' in factor:
                    multi_factor = factor.split('^')
                    multi_factor = [
                        multi_factor[0] for _ in range(int(multi_factor[1]))
                    ]
                    lines[i][1][index] = multi_factor

            lines[i][1] = flatten(lines[i][1])
            lines[i][1] = [*map(int, lines[i][1])]
            fib_factors[lines[i][0]] = lines[i][1]

            fib = next(fib_gen)

    return fib_factors


"""
It requires less computation to find the next fibonacci number than the next
Smith number. Therefore we iterate through the Fibonacci numbers, and check
if the number is also a Smith number.

The bottleneck in the algorithm is the prime factorization of the Smith number.
The third Parie number (Both Smith and Fibonacci number) is in the 10^47 range,
and is unfeasible to compute. The handy table at
http://mersennus.net/fibonacci/f1000.txt provides the factorization of the
first 1000 Fibonacci numbers.
"""

if __name__ == '__main__':
    fib_factors = load_fib_factors()

    parie_numbers = []
    fib_generator = fibonacci_generator()
    fib_num = 0

    while len(parie_numbers) < 3:
        fib_num = next(fib_generator)
        if is_smith_number(fib_num):
            parie_numbers.append(fib_num)
            print('Found Parie number:', fib_num)

    print(parie_numbers)
    print(sum(parie_numbers))
