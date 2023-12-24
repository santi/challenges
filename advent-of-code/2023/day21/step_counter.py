import numpy as np

type Spot = tuple[int, int]


def get_next_spots(garden: np.ndarray, spot: Spot) -> set[Spot]:
    x, y = spot
    spots = set()
    if x > 0 and garden[y, x - 1] in {".", "S"}:
        spots.add((x - 1, y))
    if x < garden.shape[1] - 1 and garden[y, x + 1] in {".", "S"}:
        spots.add((x + 1, y))
    if y > 0 and garden[y - 1, x] in {".", "S"}:
        spots.add((x, y - 1))
    if y < garden.shape[0] - 1 and garden[y + 1, x] in {".", "S"}:
        spots.add((x, y + 1))
    return spots


def walk_garden(garden: np.ndarray, start: Spot, steps: int) -> set[Spot]:
    current_spots: set[Spot] = set([start])
    for _ in range(steps):
        next_spots: set[Spot] = set()
        for spot in current_spots:
            next_spots.update(get_next_spots(garden, spot))
        current_spots = next_spots
    return current_spots


def main():
    with open("day21/input.txt") as f:
        lines = f.readlines()

    garden = np.array([list(line.strip()) for line in lines])
    start: Spot = tuple(np.argwhere(garden == "S")[0])

    print("Part 1:", len(walk_garden(garden, start, 64)))


if __name__ == "__main__":
    main()
