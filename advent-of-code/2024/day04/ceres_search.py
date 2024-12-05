from typing import Any
import numpy as np
from numpy.typing import NDArray

XMAS = np.array(["X", "M", "A", "S"])
SMAX = np.array(["S", "A", "M", "X"])

MAS = np.array(["M", "A", "S"])
SAM = np.array(["S", "A", "M"])

def xmas_pattern_extractor(ceres: NDArray[Any], i: int, j: int) -> list[NDArray[Any]]:
    return [
        ceres[i, j:j+4],
        ceres[i:i+4, j],
        ceres[i:i+4, j:j+4].diagonal(),
        np.fliplr(ceres[i:i+4, j:j+4]).diagonal()
    ]

def two_mas_pattern_extractor(ceres: NDArray[Any], i: int, j: int) -> list[NDArray[Any]]:
    square = ceres[i-1:i+2, j-1:j+2]
    return [square.diagonal(), np.flipud(square).diagonal()]

def matches_pattern(pattern: NDArray[Any], target: NDArray[Any]) -> bool:
    return pattern.shape == target.shape and (pattern == target).all()


def main():
    with open("day04/input.txt") as f:
        lines = f.readlines()
    puzzle = np.array([list(line.strip()) for line in lines])


    xmas_count = 0
    for i in range(puzzle.shape[0]):
        for j in range(puzzle.shape[1]):
            patterns = xmas_pattern_extractor(puzzle, i, j)
            for pattern in patterns:
                if matches_pattern(pattern, XMAS) or matches_pattern(pattern, SMAX):
                    xmas_count += 1

    print("Part 1:", xmas_count)


    two_mas_count = 0
    for i in range(1, puzzle.shape[0] - 1):
        for j in range(1, puzzle.shape[1] - 1):
            patterns = two_mas_pattern_extractor(puzzle, i, j)
            if ((patterns[0] == MAS).all() or (patterns[0] == SAM).all()) and ((patterns[1] == MAS).all() or (patterns[1] == SAM).all()):
                two_mas_count += 1

    print("Part 2:",two_mas_count)

if __name__ == "__main__":
    main()