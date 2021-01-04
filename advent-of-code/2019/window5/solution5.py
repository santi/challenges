#!/usr/bin/env python3
from os import path


def get_dir_name():
    return path.dirname(path.abspath(__file__))


def get_input():
    with open(path.join(get_dir_name(), "input5.txt"), "r") as f:
        rocket_modules = list(map(lambda m: int(m.strip()), f.readline().split(",")))
    return rocket_modules


def decode_instruction(instruction):
    instruction = str(instruction)
    op = int(instruction[-2:])

    instruction = instruction[:-2]

    op_modes = [0, 0, 0]
    given_modes = instruction[::-1]
    for index, mode in enumerate(given_modes):
        op_modes[index] = int(mode)

    return (op, op_modes)


def get_op(op_num, program, pc, op_mode):
    if op_mode:
        return program[program[pc + op_num]]
    return program[pc + op_num]


def perform_operation(program, pc, input_stream):
    op, op_modes = decode_instruction(program[pc])
    print(program)
    print(f"pc: {pc}")
    print(f"op: {op}")
    print(f"op_modes: {op_modes}")

    if op == 99:
        return program[0]
    elif op == 1:  # add, 3 parameters
        op1 = get_op(1, program, pc, op_modes[0])
        op2 = get_op(2, program, pc, op_modes[1])
        op3 = get_op(3, program, pc, op_modes[2])
        #print((program[pc], op, op_modes, (str(program[pc + 1]) + " -> " + str(operand1), str(program[pc + 2]) + " -> " + str(operand2), str(program[pc + 2]) + " -> " + str(operand3))))
        program[op3] = op1 + op2
        #print("storing " + str(operand1 + operand2) + " at position " + str(operand3))
        return perform_operation(program, pc + 4, input_stream)
    elif op == 2:  # multiply, 3 parameters
        op1 = get_op(1, program, pc, op_modes[0])
        op2 = get_op(2, program, pc, op_modes[1])
        op3 = get_op(3, program, pc, op_modes[2])
        #print((program[pc], op, op_modes, (str(program[pc + 1]) + " -> " + str(operand1), str(program[pc + 2]) + " -> " + str(operand2), str(program[pc + 2]) + " -> " + str(operand3))))
        program[op3] = op1 * op2
        #print("storing " + str(program[operand3]) + " at position " + str(operand3))
        return perform_operation(program, pc + 4, input_stream)
    elif op == 3:  # store, 1 parameter, 1 input
        op1 = get_op(1, program, pc, op_modes[0])

        #print((program[pc], op, op_modes, (str(program[pc + 1]) + " -> " + str(operand1), )))
        program[op1] = input_stream.pop()
        #print("storing 1 at position " + str(operand1))
        return perform_operation(program, pc + 2, input_stream)
    elif op == 4:  # print, 1 parameter
        op1 = get_op(1, program, pc, op_modes[0])
        #print((program[pc], op, op_modes, (str(program[pc + 1]) + " -> " + str(operand1), )))
        print(program[op1])
        return perform_operation(program, pc + 2, input_stream)
    else:
        print(op)
        raise


def part_1():
    return perform_operation(get_input(), 0, [1])


print(part_1())
