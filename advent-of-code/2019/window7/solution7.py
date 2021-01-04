#!/usr/bin/env python3
from os import path
import itertools


def get_dir_name():
    return path.dirname(path.abspath(__file__))


def get_input():
    with open(path.join(get_dir_name(), "input7_test.txt"), "r") as f:
        program = list(map(lambda m: int(m.strip()), f.readline().split(",")))
    return program


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


def run(program, inputs, outputs, pc=0):
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
            if not inputs:
                return 'NEED_INPUT', pc
            program[program[pc + 1]] = inputs.pop()
            pc += 2
        elif opcode == 4:
            op1 = _get_op1(program, pc, op1_mode)
            outputs.insert(0, op1)
            pc += 2
        elif opcode == 5:
            op1 = _get_op1(program, pc, op1_mode)
            op2 = _get_op2(program, pc, op2_mode)
            if op1 != 0:
                pc = op2
        elif opcode == 6:
            op1 = _get_op1(program, pc, op1_mode)
            op2 = _get_op2(program, pc, op2_mode)
            if op1 == 0:
                pc = op2
        elif opcode == 7:
            op1 = _get_op1(program, pc, op1_mode)
            op2 = _get_op2(program, pc, op2_mode)
            dest = program[pc + 3]
            
            program[dest] = 1 if op1 < op2 else 0
            pc += 4
        elif opcode == 8:
            op1 = _get_op1(program, pc, op1_mode)
            op2 = _get_op2(program, pc, op2_mode)
            dest = program[pc + 3]
            
            program[dest] = 1 if op1 == op2 else 0
            pc += 4
        elif opcode == 99:
            break
        else:
            print('unknown opcode')
            print('processed ' + str(pc))
            print('opcode: ' + str(opcode))
            raise
            break
    return 'HALT', None

# solution_1 = 24625

program = get_input()
#print(program)
#print(run(program, [8]))
max_output = 0

# print(run(program, [run(program, [run(program, [run(program, [run(program, [0, 0]), 4]), 3]), 2]), 1]))
for permutation in list(itertools.permutations([5, 6, 7, 8, 9])):
    a, b, c, d, e = permutation
    pc_a = 0
    pc_b = 0
    pc_c = 0
    pc_d = 0
    pc_e = 0
    input_a = [0, a]
    input_b = [b]
    input_c = [c]
    input_d = [d]
    input_e = [e]

    while True:
        output_a, pc_a = run(program, input_a, input_b, pc_a)
        output_b, pc_b = run(program, input_b, input_c, pc_b)
        output_c, pc_c = run(program, input_c, input_d, pc_c)
        output_d, pc_d = run(program, input_d, input_e, pc_d)
        output_e_temp, pc_e = run(program, input_e, input_a, pc_e)
        if output_e_temp == 'HALT':
            break
    print(input_a)
    #max_output = max(output_e, max_output)
        
print(max_output)
