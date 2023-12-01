import re
from re import Pattern

numerical_value = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def calibration_value(line: str, pattern: Pattern) -> int:
    matches = pattern.findall(line)
    return int(f"{numerical_value[matches[0]]}{numerical_value[matches[-1]]}")


pattern_part1 = re.compile(r"(\d)")
pattern_part2 = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")

with open("input.txt") as f:
    lines = f.readlines()
    print("Part 1:", sum(calibration_value(line, pattern_part1) for line in lines))
    print("Part 2:", sum(calibration_value(line, pattern_part2) for line in lines))
