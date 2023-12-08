import re
from collections import namedtuple
from typing import Literal


Node = namedtuple("Node", ["L", "R"])
type Direction = Literal["L"] | Literal["R"]

map_pattern = re.compile(r"(?P<name>\w{3}).*(?P<left>\w{3}), (?P<right>\w{3})")


def next_nodes(
    map: dict[str, dict[Direction, str]], current_nodes: set[str], direction: Direction
) -> set[str]:
    return set(map[node][direction] for node in current_nodes)


def main():
    with open("day07/test.txt") as f:
        lines = f.readlines()
        directions = lines[0].strip()

        nodes = {}
        for line in lines[2:]:
            name, left, right = map_pattern.match(line).groups()
            nodes[name] = {"L": left, "R": right}
        # steps = 0
        # current_node = "AAA"
        # while current_node != "ZZZ":
        #     direction = directions[steps % len(directions)]
        #     current_node = nodes[current_node][direction]
        #     steps += 1
        # print("Part 1:", steps)

        steps = 0
        current_nodes = set(node for node in nodes.keys() if node[-1] == "A")
        while any(node[-1] != "Z" for node in current_nodes):
            direction: Direction = directions[steps % len(directions)]
            current_nodes = next_nodes(nodes, current_nodes, direction)
            steps += 1
        print("Part 2:", steps)


if __name__ == "__main__":
    main()
