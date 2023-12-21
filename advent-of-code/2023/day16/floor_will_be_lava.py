import sys
from enum import Enum

sys.setrecursionlimit(10_000)

type Position = tuple[int, int]


class Direction(str, Enum):
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


def move_up(position: Position) -> Position:
    x, y = position
    return (x, y - 1)


def move_down(position: Position) -> Position:
    x, y = position
    return (x, y + 1)


def move_left(position: Position) -> Position:
    x, y = position
    return (x - 1, y)


def move_right(position: Position) -> Position:
    x, y = position
    return (x + 1, y)


def next_position(position: Position, direction: Direction) -> Position:
    x, y = position
    if direction == Direction.UP:
        return move_up(position)
    elif direction == Direction.DOWN:
        return move_down(position)
    elif direction == Direction.LEFT:
        return move_left(position)
    elif direction == Direction.RIGHT:
        return move_right(position)
    else:
        raise ValueError(f"Invalid direction: {direction}")


def visit(
    grid: list[list[str]],
    position: Position,
    direction: Direction,
    visited: set[tuple[Position, Direction]],
):
    x, y = position
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
        return

    if (position, direction) in visited:
        return
    visited.add((position, direction))

    if grid[y][x] == ".":
        return visit(grid, next_position(position, direction), direction, visited)
    elif grid[y][x] == "/":
        if direction == Direction.UP:
            return visit(grid, next_position(position, Direction.RIGHT), Direction.RIGHT, visited)
        elif direction == Direction.DOWN:
            return visit(grid, next_position(position, Direction.LEFT), Direction.LEFT, visited)
        elif direction == Direction.LEFT:
            return visit(grid, next_position(position, Direction.DOWN), Direction.DOWN, visited)
        elif direction == Direction.RIGHT:
            return visit(grid, next_position(position, Direction.UP), Direction.UP, visited)
    elif grid[y][x] == "\\":
        if direction == Direction.UP:
            return visit(grid, next_position(position, Direction.LEFT), Direction.LEFT, visited)
        elif direction == Direction.DOWN:
            return visit(grid, next_position(position, Direction.RIGHT), Direction.RIGHT, visited)
        elif direction == Direction.LEFT:
            return visit(grid, next_position(position, Direction.UP), Direction.UP, visited)
        elif direction == Direction.RIGHT:
            return visit(grid, next_position(position, Direction.DOWN), Direction.DOWN, visited)
    elif grid[y][x] == "-":
        if direction in {Direction.LEFT, Direction.RIGHT}:
            return visit(grid, next_position(position, direction), direction, visited)
        else:
            visit(grid, next_position(position, Direction.LEFT), Direction.LEFT, visited)
            visit(grid, next_position(position, Direction.RIGHT), Direction.RIGHT, visited)
            return
    elif grid[y][x] == "|":
        if direction in {Direction.UP, Direction.DOWN}:
            return visit(grid, next_position(position, direction), direction, visited)
        else:
            visit(grid, next_position(position, Direction.UP), Direction.UP, visited)
            visit(grid, next_position(position, Direction.DOWN), Direction.DOWN, visited)
            return


def main():
    with open("day16/input.txt") as f:
        lines = f.readlines()
    grid: list[list[str]] = [list(line.strip()) for line in lines]

    visited: set[tuple[Position, Direction]] = set()
    visit(grid, (0, 0), Direction.RIGHT, visited)
    print("Part 1:", len(set(p for p, _ in visited)))


if __name__ == "__main__":
    main()
