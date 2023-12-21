import numpy as np
from numpy import bool_
from numpy.typing import NDArray


def equal(pattern1: NDArray, pattern2: NDArray) -> bool_:
    return np.all(pattern1 == pattern2)


def are_mirrors(pattern1: NDArray, pattern2: NDArray) -> bool_:
    pattern1 = np.flip(pattern1, axis=0)
    cutoff = min(pattern1.shape[0], pattern2.shape[0])

    pattern1 = pattern1[0:cutoff, :]
    pattern2 = pattern2[0:cutoff, :]

    return np.all(pattern1 == pattern2)


def parse_patterns(lines: list[str]) -> list[NDArray]:
    patterns: list[NDArray] = []
    pattern: list[list[str]] = []
    for line in lines:
        line = line.strip()

        if line == "":
            patterns.append(np.array(pattern))
            pattern = []
            continue

        pattern.append(list(line))

    patterns.append(np.array(pattern))
    return patterns


def scan_reflections(pattern: NDArray, multiplier: int, skip_value: int) -> int:
    last_row = np.array(pattern[0])
    for i, row in enumerate(pattern[1:], 1):
        if equal(row, last_row) and are_mirrors(pattern[0:i], pattern[i:]):
            reflection_value = i * multiplier
            if skip_value == reflection_value:
                continue
            return i * multiplier
        last_row = row
    return 0


def get_reflection_value(pattern: NDArray, skip_value: int = 0) -> int:
    if reflection_value := scan_reflections(pattern, 100, skip_value):
        return reflection_value

    pattern = pattern.transpose()

    if reflection_value := scan_reflections(pattern, 1, skip_value):
        return reflection_value

    return 0


def get_clean_reflection_value(pattern: NDArray) -> int:
    original_reflection_value = get_reflection_value(pattern)
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            clean_pattern = np.copy(pattern)
            if clean_pattern[i][j] == "#":
                clean_pattern[i][j] = "."
            elif clean_pattern[i][j] == ".":
                clean_pattern[i][j] = "#"
            else:
                raise ValueError("Invalid pattern value!")
            if reflection_value := get_reflection_value(clean_pattern, original_reflection_value):
                return reflection_value

    raise ValueError("No pattern found!")


def main():
    with open("day13/input.txt") as f:
        lines = f.readlines()
    patterns = parse_patterns(lines)
    print("Part 1:", sum(get_reflection_value(pattern) for pattern in patterns))
    print("Part 2:", sum(get_clean_reflection_value(pattern) for pattern in patterns))


if __name__ == "__main__":
    main()
