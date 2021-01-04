#!/usr/bin/env python3
from os import path


def get_dir_name():
    return path.dirname(path.abspath(__file__))


def get_input():
    with open(path.join(get_dir_name(), "input5.txt"), "r") as f:
        rocket_modules = list(map(lambda m: int(m.strip()), f.readline().split(",")))
    return rocket_modules


def _decode_opcode(num):
    digits = [0, 0, 0, 0, 0]
    pos = len(digits) - 1
    while num > 0 and pos >= 0:
        digits[pos] = num % 10
        num //= 10
        pos -= 1
    return digits


def _get_op1(program, pc, mode):
    return program[program[pc + 1]] if mode == 0 else program[pc + 1]


def _get_op2(program, pc, mode):
    return program[program[pc + 2]] if mode == 0 else program[pc + 2]


def get_program(file):
    with open(file) as f:
        return list(map(int, f.read().split(',')))


def run(program, input_id):
    diagnostic_code = 0
    pc = 0
    while pc < len(program):
        opcode_obj = _decode_opcode(program[pc])
        opcode = opcode_obj[3] * 10 + opcode_obj[4]
        op1_mode = opcode_obj[2]
        op2_mode = opcode_obj[1]
        if opcode == 1 or opcode == 2:
            op1, op2 = _get_op1(program, pc, op1_mode), _get_op2(program, pc, op2_mode)
            dest = program[pc + 3]
            program[dest] = op1 + op2 if opcode == 1 else op1 * op2
            pc += 4
        elif opcode == 3:
            program[program[pc + 1]] = input_id
            pc += 2
        elif opcode == 4:
            op1 = _get_op1(program, pc, op1_mode)
            diagnostic_code = op1
            pc += 2
        elif opcode == 99:
            break
        else:
            print('unknown opcode')
            break
    return diagnostic_code


print(run(get_input(), 1))  # 8332629
print(run(get_input(), 5))  # 8332629