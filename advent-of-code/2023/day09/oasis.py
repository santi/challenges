from enum import Enum


class Direction(Enum):
    START = 0
    END = -1


def get_differences(inputs: list[int]):
    differences = list()
    for i in range(1, len(inputs)):
        differences.append(inputs[i] - inputs[i - 1])
    return differences


def interpolate_value(reading: list[int], direction: Direction):
    differences = [reading, get_differences(reading)]
    while not all(difference == 0 for difference in differences[-1]):
        differences.append(get_differences(differences[-1]))

    for i in range(len(differences) - 1, 0, -1):
        current_differences = differences[i][direction.value]
        previous_differences = differences[i - 1][direction.value]

        differences[i - 1].insert(
            len(differences[i - 1]) if direction == Direction.END else 0,
            current_differences + previous_differences
            if direction == Direction.END
            else previous_differences - current_differences,
        )
    return differences[0][direction.value]


def main():
    with open("day09/input.txt") as f:
        lines = f.readlines()
        readings = list(list(map(int, line.strip().split(" "))) for line in lines)

        print("Part 1:", sum(interpolate_value(reading, Direction.END) for reading in readings))
        print("Part 2:", sum(interpolate_value(reading, Direction.START) for reading in readings))


if __name__ == "__main__":
    main()
