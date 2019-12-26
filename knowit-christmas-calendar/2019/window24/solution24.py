#!/usr/bin/env python3

MAX_X = 203
MAX_Y = 342


def print_map(_map): 
    print("\n" + "-" * MAX_X + "\n")
    for line in _map:
        print("".join(line))


with open("input24.txt") as f:
    coordinates = []
    _map = [["." for _ in range(MAX_X)] for _ in range(MAX_Y)]
    for line in f.readlines():
        line = line.strip()
        if line == '---':
            print_map(_map)
            coordinates = []
            _map = [["." for _ in range(MAX_X)] for _ in range(MAX_Y)]
            continue

        c1, c2 = line.split(",")
        _map[MAX_Y - int(c2)][int(c1)] = "X"
