import numpy as np
from numpy import bool_
from numpy.typing import NDArray
from itertools import combinations


def span_empty(row: NDArray, expansion_rate: int) -> bool_:
    return np.all(np.isin(row, [".", expansion_rate]))


def expand_universe(universe: NDArray, expansion_rate: int) -> NDArray:
    expanded_universe = np.empty(universe.shape, dtype=int)
    for i in range(len(universe)):
        empty_row = span_empty(universe[i, :], expansion_rate)
        for j in range(len(universe[i])):
            empty_col = span_empty(universe[:, j], expansion_rate)
            if empty_col or empty_row:
                expanded_universe[i, j] = expansion_rate
            elif universe[i, j] in {"#", "."}:
                expanded_universe[i, j] = 1

    return expanded_universe


def distance(universe: NDArray, a: tuple[int, int], b: tuple[int, int]) -> int:
    vertical_path = universe[min(a[0], b[0]) : max(a[0], b[0]), b[1]]
    horizontal_path = universe[a[0], min(a[1], b[1]) : max(a[1], b[1])]

    return np.sum(vertical_path) + np.sum(horizontal_path)


def get_galaxies(universe: NDArray) -> dict[str, tuple[int, int]]:
    galaxies: dict[str, tuple[int, int]] = {}
    galaxy_index = 1
    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if universe[i, j] == "#":
                galaxies[f"{galaxy_index}"] = (i, j)
                galaxy_index += 1

    return galaxies


def main():
    with open("day11/input.txt") as f:
        lines = f.readlines()
        universe = np.array([list(line.strip()) for line in lines])
        galaxies = get_galaxies(universe)
        combos = list(comb for comb in combinations(galaxies.keys(), 2))

        expanded_universe = expand_universe(universe, 2)
        print(
            "Part 1:", sum(distance(expanded_universe, galaxies[a], galaxies[b]) for a, b in combos)
        )

        expanded_universe = expand_universe(universe, 1_000_000)
        print(
            "Part 2:", sum(distance(expanded_universe, galaxies[a], galaxies[b]) for a, b in combos)
        )


if __name__ == "__main__":
    main()
