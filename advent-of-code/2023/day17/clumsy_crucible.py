import sys
from enum import Enum
from queue import PriorityQueue

sys.setrecursionlimit(100_000)

type Position = tuple[int, int]
type Momentum = tuple[Direction, int]
type Node = tuple[Position, Momentum]


class Direction(str, Enum):
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


def get_neighbours(
    city: list[list[int]],
    node: Node,
    heat_loss: int,
    minimum_speed: int = 0,
    maximum_speed: int = 3,
) -> list[tuple[int, Node]]:
    neighbours: list[tuple[int, Node]] = []
    position, momentum = node
    x, y = position
    direction, speed = momentum

    nodes: list[Node] = []
    if speed >= minimum_speed:
        if direction == Direction.UP:
            nodes.append(((x + 1, y), (Direction.RIGHT, 1)))
            nodes.append(((x - 1, y), (Direction.LEFT, 1)))
        elif direction == Direction.DOWN:
            nodes.append(((x + 1, y), (Direction.RIGHT, 1)))
            nodes.append(((x - 1, y), (Direction.LEFT, 1)))
        elif direction == Direction.LEFT:
            nodes.append(((x, y + 1), (Direction.DOWN, 1)))
            nodes.append(((x, y - 1), (Direction.UP, 1)))
        elif direction == Direction.RIGHT:
            nodes.append(((x, y + 1), (Direction.DOWN, 1)))
            nodes.append(((x, y - 1), (Direction.UP, 1)))

    if speed < maximum_speed:
        if momentum[0] == Direction.UP:
            nodes.append(((x, y - 1), (Direction.UP, speed + 1)))
        elif momentum[0] == Direction.DOWN:
            nodes.append(((x, y + 1), (Direction.DOWN, speed + 1)))
        elif momentum[0] == Direction.LEFT:
            nodes.append(((x - 1, y), (Direction.LEFT, speed + 1)))
        elif momentum[0] == Direction.RIGHT:
            nodes.append(((x + 1, y), (Direction.RIGHT, speed + 1)))

    # Remove the nodes that are out of bounds
    nodes = [
        node for node in nodes if 0 <= node[0][0] < len(city[0]) and 0 <= node[0][1] < len(city)
    ]

    for node in nodes:
        position, _ = node
        x, y = position
        neighbours.append((heat_loss + city[y][x], node))

    return neighbours


def crucible_shortest_path(
    city: list[list[int]],
    queue: PriorityQueue[tuple[int, Node]],
    minimum_speed: int,
    maximum_speed: int,
) -> int:
    visited: set[Node] = set()

    while not queue.empty():
        heat_loss, node = queue.get()

        if node in visited:
            continue
        visited.add(node)

        position, _ = node
        if position == (len(city[0]) - 1, len(city) - 1):
            return heat_loss

        for neighbour in get_neighbours(city, node, heat_loss, minimum_speed, maximum_speed):
            queue.put(neighbour)
    raise ValueError("No path found")


def main():
    with open("day17/input.txt") as f:
        lines = f.readlines()
    city: list[list[int]] = [list(map(int, list(line.strip()))) for line in lines]

    queue: PriorityQueue[tuple[int, Node]] = PriorityQueue()
    queue.put((0, ((0, 0), (Direction.RIGHT, 0))))
    print("Part 1:", crucible_shortest_path(city, queue, 0, 3))

    queue: PriorityQueue[tuple[int, Node]] = PriorityQueue()
    queue.put((0, ((0, 0), (Direction.RIGHT, 0))))
    queue.put((0, ((0, 0), (Direction.DOWN, 0))))
    print("Part 2:", crucible_shortest_path(city, queue, 4, 10))


if __name__ == "__main__":
    main()
