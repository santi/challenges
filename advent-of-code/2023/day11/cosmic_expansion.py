from itertools import combinations


def is_row_empty(row: list[str]) -> bool:
    return all([point == "." for point in row])


def expand_universe(universe: list[list[str]]) -> list[list[str]]:
    i = 0
    while i < len(universe):
        if is_row_empty(universe[i]):
            universe.insert(i, ["." for _ in range(len(universe[i]))])
            i += 1
        i += 1
    i = 0
    while i < len(universe[0]):
        if is_row_empty([row[i] for row in universe]):
            for row in universe:
                row.insert(i, ".")
            i += 1
        i += 1
    return universe


def distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_galaxies(universe: list[list[str]]) -> dict[str, tuple[int, int]]:
    galaxies: dict[str, tuple[int, int]] = {}
    galaxy_index = 1
    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if universe[i][j] == "#":
                galaxies[f"{galaxy_index}"] = (i, j)
                galaxy_index += 1

    return galaxies


def main():
    with open("day11/input.txt") as f:
        lines = f.readlines()
        universe = [list(line.strip()) for line in lines]
        for row in universe:
            print("".join(row))
        universe = expand_universe(universe)
        for row in universe:
            print("".join(row))
        galaxies = get_galaxies(universe)
        combos = list(comb for comb in combinations(galaxies.keys(), 2))
        print(sum(distance(galaxies[a], galaxies[b]) for a, b in combos))


if __name__ == "__main__":
    main()
