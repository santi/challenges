import re
from collections import namedtuple


Node = namedtuple("Node", ["L", "R"])

map_pattern = re.compile(r"(?P<name>\w{3}).*(?P<left>\w{3}), (?P<right>\w{3})")


def main():
    with open("day07/input.txt") as f:
        lines = f.readlines()
        directions = lines[0].strip()

        nodes = {}
        for line in lines[2:]:
            name, left, right = map_pattern.match(line).groups()
            nodes[name] = {"L": left, "R": right}
        print(nodes)
        steps = 0
        current_node = "AAA"
        while current_node != "ZZZ":
            direction = directions[steps % len(directions)]
            current_node = nodes[current_node][direction]
            steps += 1
        print(steps)


if __name__ == "__main__":
    main()
