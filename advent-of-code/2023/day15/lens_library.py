import re
from collections import defaultdict

lens_pattern = re.compile(r"(\w+)([-=])(\d+)?")


def HASH(line: str) -> int:
    value = 0
    for char in line:
        value += ord(char)
        value *= 17
        value %= 256
    return value


def replace(box: list[str], label: str, focal_length: str) -> bool:
    for i, lens in enumerate(box):
        if lens.split(" ")[0] == label:
            box[i] = f"{label} {focal_length}"
            return True
    return False


def HASHMAP(lenses: list[str]) -> dict[int, list[str]]:
    boxes: dict[int, list[str]] = defaultdict(list)
    for lens in lenses:
        label, operation, focal_length = lens_pattern.match(lens).groups()
        box_number = HASH(label)
        box = boxes[box_number]
        if operation == "-":
            boxes[box_number] = [l for l in box if l.split(" ")[0] != label]
        elif operation == "=":
            if not replace(box, label, focal_length):
                box.append(f"{label} {focal_length}")

    return boxes


def focus_power(box_number: int, box: list[str]) -> int:
    power = 0
    for i, lens in enumerate(box, 1):
        _, focal_length = lens.split(" ")
        power += (box_number + 1) * i * int(focal_length)
    return power


def main():
    with open("day15/input.txt") as f:
        lines = f.readline().strip().split(",")
    print("Part 1:", sum(HASH(l) for l in lines))
    print("Part 2:", sum(focus_power(*box) for box in HASHMAP(lines).items()))


if __name__ == "__main__":
    main()
