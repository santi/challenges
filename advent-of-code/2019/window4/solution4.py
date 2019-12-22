#!/usr/bin/env python3
from os import path
from functools import reduce


def get_dir_name():
    return path.dirname(path.abspath(__file__))


def get_input():
    with open(path.join(get_dir_name(), "input4.txt"), "r") as f:
        bounds = f.readline().split("-")
        lower_bound, higher_bound = int(bounds[0]), int(bounds[1])
    return (lower_bound, higher_bound)


def is_increasing(number):
    number = str(number)
    return number == "".join(sorted(number))


def _check_double_digits(number, last_digit):
    if len(number) == 0:
        return False
    if last_digit == number[0]:
        return True
    return _check_double_digits(number[1:], number[0])


def has_double_digits(number):
    number = str(number)
    return _check_double_digits(number, None)


def num_increasing_and_double_digits(lower, higher):
    """
    Not really possibly to do recursively in Python because of missing
    tail call optimization. It is possible to make a hack around it,
    but it eats away on performance and should be avoided.
    """
    counter = 0
    for i in range(lower, higher):
        if is_increasing(i) and has_double_digits(i):
            counter += 1
    return counter


def part_1():
    return num_increasing_and_double_digits(*get_input())


print(part_1())  # 1929


def _check_double_digits_but_not_more(number, last_digit, has_double, skip_until_new_digit):
    if number == "":
        return has_double

    digit = number[:1]

    if skip_until_new_digit and digit == last_digit:
        return _check_double_digits_but_not_more(number[1:], digit, False, True)

    if has_double:
        if digit == last_digit:
            return _check_double_digits_but_not_more(number[1:], digit, False, True)
        return True

    else:
        if digit == last_digit:
            return _check_double_digits_but_not_more(number[1:], digit, True, False)
        return _check_double_digits_but_not_more(number[1:], digit, False, False)


def has_double_digits_but_not_more(number):
    number = str(number)
    return _check_double_digits_but_not_more(number, None, False, False)



def num_increasing_and_only_double_digits(lower, higher):
    reduce
    counter = 0
    for i in range(lower, higher):
        if is_increasing(i) and has_double_digits_but_not_more(i):
            counter += 1
    return counter


def part_2():
    return num_increasing_and_only_double_digits(*get_input())


print(part_2())  # 1306
