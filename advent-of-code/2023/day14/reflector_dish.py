import numpy as np
from numpy.typing import NDArray


def search(platform: NDArray[np.str_], y: int) -> int:
    if y == -1:
        return 0
    if platform[y] != ".":
        return y + 1
    return search(platform, y - 1)


def move(platform: NDArray[np.str_], x: int, y: int) -> NDArray[np.str_]:
    column = platform[:, x]
    move_to = search(column, y - 1)
    platform[y][x] = "."
    platform[move_to][x] = "O"
    return platform


def rotate(platform: NDArray[np.str_], cycles: int = 1_000_000_000) -> NDArray[np.str_]:
    cache: dict[int, int] = {}

    cycle = 0
    while cycle < cycles:
        for _ in range(4):
            platform = tilt(platform)
            platform = np.rot90(platform, 3)
        cycle += 1

        platform_hash = hash("".join(platform.flatten()))
        if platform_hash in cache:
            cycle_length = cycle - cache[platform_hash]
            cycle += ((cycles - cycle) // cycle_length) * cycle_length
            continue
        else:
            cache[platform_hash] = cycle
    return platform


def tilt(platform: NDArray[np.str_]) -> NDArray[np.str_]:
    for y in range(len(platform)):
        for x in range(len(platform[y])):
            if platform[y][x] == "O":
                platform = move(platform, x, y)

    return platform


def support_beam_load(platform: NDArray[np.str_]) -> int:
    return sum(
        np.count_nonzero(row == "O") * multiplier
        for multiplier, row in enumerate(np.flip(platform), 1)
    )


def main():
    with open("day14/input.txt") as f:
        lines = f.readlines()
    platform: NDArray[np.str_] = np.array([list(line.strip()) for line in lines])
    print("Part 1:", support_beam_load(tilt(platform)))
    print("Part 2:", support_beam_load(rotate(platform)))


if __name__ == "__main__":
    main()
