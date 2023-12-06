from functools import reduce
from operator import add, mul


def ways_to_win(time: int, distance: int) -> int:
    winning_strategies = 0
    speed = 0
    for i in range(1, time):
        speed += 1
        if speed * (time - i) > distance:
            winning_strategies += 1
    return winning_strategies


def main():
    with open("day06/input.txt") as f:
        lines = f.readlines()
        times = [int(time) for time in lines[0].strip().split(" ") if time.isnumeric()]
        distances = [
            int(distance) for distance in lines[1].strip().split(" ") if distance.isnumeric()
        ]

        complete_time = int(reduce(add, (str(time) for time in times)))
        complete_distance = int(reduce(add, (str(distance) for distance in distances)))

        print(
            "Part 1:",
            reduce(mul, (ways_to_win(time, distance) for time, distance in zip(times, distances))),
        )
        print("Part 2:", ways_to_win(complete_time, complete_distance))


if __name__ == "__main__":
    main()
