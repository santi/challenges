#!/usr/bin/env python3
from os import path


def get_dir_name():
    return path.dirname(path.abspath(__file__))


with open(path.join(get_dir_name(), "input1.txt"), "r") as f:
    rocket_modules = list(map(lambda m: int(m.strip()), f.readlines()))


def get_required_fuel(mass):
    return int(mass / 3) - 2


def part_1():
    return sum(map(get_required_fuel, rocket_modules))


print(part_1())


def get_required_fuel_expanded(mass):
    required_fuel = get_required_fuel(mass)
    fuel = required_fuel
    while required_fuel > 0:
        required_fuel = get_required_fuel(required_fuel)
        if required_fuel > 0:
            fuel += required_fuel
    return fuel


def part_2():
    return sum(map(get_required_fuel_expanded, rocket_modules))


print(part_2())
