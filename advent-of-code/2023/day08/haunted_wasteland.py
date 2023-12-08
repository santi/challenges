import re
from math import lcm
from collections import namedtuple
from typing import Callable, Literal

Node = namedtuple("Node", ["L", "R"])
type Direction = Literal["L", "R"]

map_pattern = re.compile(r"(?P<name>\w{3}).*(?P<left>\w{3}), (?P<right>\w{3})")


def distance_to_goal(
    map: dict[str, dict[Direction, str]],
    node: str,
    directions: str,
    goal_checker: Callable[[str], bool],
) -> int:
    steps = 0
    current_node = node
    while not goal_checker(current_node):
        direction = directions[steps % len(directions)]
        current_node = map[current_node][direction]
        steps += 1
    return steps


def main():
    with open("day08/input.txt") as f:
        lines = f.readlines()
        directions = lines[0].strip()

        nodes = {}
        for line in lines[2:]:
            name, left, right = map_pattern.match(line).groups()
            nodes[name] = {"L": left, "R": right}

        print("Part 1:", distance_to_goal(nodes, "AAA", directions, lambda node: node == "ZZZ"))
        print(
            "Part 2:",
            lcm(
                *(
                    distance_to_goal(nodes, node, directions, lambda node: node[-1] == "Z")
                    for node in nodes.keys()
                    if node[-1] == "A"
                )
            ),
        )


if __name__ == "__main__":
    main()
