#!/usr/bin/env python3
from os import path


def get_dir_name():
    return path.dirname(path.abspath(__file__))


def get_input():
    with open(path.join(get_dir_name(), "input2.txt"), "r") as f:
        return list(map(lambda m: int(m.strip()), f.readline().split(",")))


def run(program, pc):
    if program[pc] == 99:
        return program[0]
    elif program[pc] == 1:
        program[program[pc + 3]] = program[program[pc + 1]] + program[program[pc + 2]]
        return run(program, pc + 4)
    elif program[pc] == 2:
        program[program[pc + 3]] = program[program[pc + 1]] * program[program[pc + 2]]
        return run(program, pc + 4)
    else:
        raise 


def part_1():
    program = get_input()
    program[1] = 12
    program[2] = 2

    return run(program, 0)


print(part_1())  # 4570637


def part_2():
    for noun in range(100):
        for verb in range(100):
            program = get_input()
            program[1] = noun
            program[2] = verb
            if run(program, 0) == 19_690_720:
                return 100 * noun + verb


print(part_2())  # 5485
