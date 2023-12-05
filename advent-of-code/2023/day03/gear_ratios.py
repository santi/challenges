import numpy as np
from pydantic import BaseModel
from numpy.typing import NDArray

characters = np.array([".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])


class EnginePart(BaseModel):
    start: int
    end: int
    number: int


def get_engine_parts_on_line(lines: NDArray, row_no: int) -> list[EnginePart]:
    engine_parts: list[EnginePart] = []
    current_digits = ""
    is_engine_part = False
    for col_no in range(0, len(lines[row_no])):
        if lines[row_no][col_no].isdigit():
            current_digits += lines[row_no][col_no]
            if not is_engine_part:
                square_3x3 = lines[row_no - 1 : row_no + 2, col_no - 1 : col_no + 2]
                is_engine_part = np.count_nonzero(np.isin(square_3x3, characters)) != 9
        else:
            if is_engine_part and current_digits:
                engine_parts.append(
                    EnginePart(
                        start=col_no - len(current_digits),
                        end=col_no - 1,
                        number=int(current_digits),
                    )
                )
            is_engine_part = False
            current_digits = ""
    is_engine_part = False
    return engine_parts


def get_engine_part_sum(lines: NDArray) -> int:
    engine_part_sum = 0
    for row_no in range(1, len(lines) - 1):
        engine_parts = get_engine_parts_on_line(lines, row_no)
        engine_part_sum += sum([engine.number for engine in engine_parts])
    return engine_part_sum


def get_gear_ratio(lines: NDArray) -> int:
    gear_ratio = 0
    for row_no in range(1, len(lines) - 1):
        gear_ratio += get_gear_ratio_for_line(lines, row_no)

    return gear_ratio


def adjacent_engine_parts(col_no: int, engine_parts: list[EnginePart]) -> list[EnginePart]:
    return [
        engine_part
        for engine_part in engine_parts
        if engine_part.start - 1 <= col_no <= engine_part.end + 1
    ]


def get_gear_ratio_for_line(lines: NDArray, row_no: int) -> int:
    engine_parts: list[EnginePart] = []
    for row in range(row_no - 1, row_no + 2):
        engine_parts += get_engine_parts_on_line(lines, row)

    gear_ratio = 0
    for col_no in range(1, len(lines[row_no]) - 1):
        if lines[row_no][col_no] == "*":
            close_engine_parts = adjacent_engine_parts(col_no, engine_parts)
            if len(close_engine_parts) == 2:
                gear_ratio += close_engine_parts[0].number * close_engine_parts[1].number

    return gear_ratio


def main():
    with open("day03/input.txt") as f:
        lines = f.readlines()
        lines = [list(line.strip()) for line in lines]
        lines = np.array(lines, dtype=str)
        lines = np.pad(lines, 1, constant_values=".")

        print("Part 1:", get_engine_part_sum(lines))
        print("Part 2:", get_gear_ratio(lines))


if __name__ == "__main__":
    main()
