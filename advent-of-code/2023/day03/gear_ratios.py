import numpy as np
from numpy.typing import NDArray

characters = np.array(['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

with open("day03/input.txt") as f:
    lines = f.readlines()
    lines = [list(line.strip()) for line in lines]
    lines = np.array(lines, dtype=str)
    lines = np.pad(lines, 1, constant_values='.')

    engine_part_sum = 0

    current_digits = ''
    is_engine_part = False
    for row_no in range(1, len(lines) - 1):
        for col_no in range(1, len(lines[row_no]) - 1):
            if lines[row_no][col_no].isdigit():
                current_digits += lines[row_no][col_no]
                if not is_engine_part:
                    square_3x3 = lines[row_no - 1:row_no + 2, col_no - 1:col_no + 2]
                    num_dots = np.count_nonzero(np.isin(square_3x3, characters))
                    if num_dots != 9:
                        print('found engine part!')
                        is_engine_part = True
            else:
                print('found something else. No longer an engine_part.')
                if is_engine_part and current_digits:
                    print(current_digits, 'is an engine part')
                    engine_part_sum += int(current_digits)
                is_engine_part = False
                current_digits = ''

        if is_engine_part and current_digits:
            print(current_digits, 'is an engine part')
            engine_part_sum += int(current_digits)
            current_digits = ''
        is_engine_part = False
    print(engine_part_sum)





def get_adjacent_parts(line: NDArray) -> int:
    pass
with open("day03/input.txt") as f:
    lines = f.readlines()
    lines = [list(line.strip()) for line in lines]
    lines = np.array(lines, dtype=str)
    lines = np.pad(lines, 1, constant_values='.')

    for row_no in range(1, len(lines) - 1):
        for col_no in range(1, len(lines[row_no]) - 1):
            if lines[row_no][col_no] == '*':
                    square_3x3 = lines[row_no - 1:row_no + 2, col_no - 1:col_no + 2]









