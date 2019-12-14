#!/usr/bin/env python3
from os import path
import sys
sys.setrecursionlimit(10_000)

RIGHT = 'R'
LEFT = 'L'
UP = 'U'
DOWN = 'D'


def get_dir_name():
    return path.dirname(path.abspath(__file__))


def get_input():
    with open(path.join(get_dir_name(), "input3.txt"), "r") as f:
        line1 = f.readline().split(",")
        line2 = f.readline().split(",")
    return (line1, line2)


def manhattan_distance(point1, point2):
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])


def distance_from_origo(point):
    return manhattan_distance((0, 0), point)


def walk_segment(x, y, distance, direction, length, visited, crossings, shortest_distance, update_shortest_distance):
    if length == 0:
        return (x, y, distance, visited, shortest_distance)
    
    if direction == RIGHT:
        location = (x + 1, y)
    elif direction == LEFT:
        location = (x - 1, y)
    elif direction == UP:
        location = (x, y + 1)
    elif direction == DOWN:
        location = (x, y - 1)

    shortest_distance = update_shortest_distance(crossings, location, distance, shortest_distance)
    visited[location] = min(distance + 1, visited.get(location, sys.maxsize))
    return walk_segment(
        *location,
        distance + 1,
        direction,
        length - 1,
        visited,
        crossings,
        shortest_distance,
        update_shortest_distance)


def walk_wire(wire, x, y, distance, visited, crossings, shortest_distance, update_shortest_distance):
    if len(wire) == 0:
        return visited, shortest_distance
    segment = wire[0]
    direction, length = decode_segment(segment)
    x, y, distance, visited, shortest_distance = walk_segment(
                                                    x,
                                                    y,
                                                    distance,
                                                    direction,
                                                    length,
                                                    visited,
                                                    crossings,
                                                    shortest_distance,
                                                    update_shortest_distance)

    return walk_wire(wire[1:], x, y, distance, visited, crossings, shortest_distance, update_shortest_distance)


def decode_segment(segment):
    direction = segment[0]
    length = int(segment[1:])
    return (direction, length)


def manhattan_solver(wire1, wire2):
    def update_shortest_distance(crossings, location, distance, shortest_distance):
        if crossings.get(location):
            return min(distance_from_origo(location), shortest_distance)
        return shortest_distance

    wire1_visited, _ = walk_wire(wire1, 0, 0, 0, dict(), dict(), 0, update_shortest_distance)
    _, shortest_distance = walk_wire(wire2, 0, 0, 0, dict(), wire1_visited, sys.maxsize, update_shortest_distance)
    return shortest_distance


def part_1():
    line1, line2 = get_input()
    return manhattan_solver(line1, line2)


print(part_1())  # 3229


def length_solver(wire1, wire2):

    def update_shortest_distance(crossings, location, distance, shortest_distance):
        if crossings.get(location):
            shortest_distance = min(crossings[location] + distance + 1, shortest_distance)
        return shortest_distance

    crossings, _ = walk_wire(wire1, 0, 0, 0, dict(), dict(), 0, update_shortest_distance)
    _, shortest_distance = walk_wire(wire2, 0, 0, 0, dict(), crossings, sys.maxsize, update_shortest_distance)
    return shortest_distance


def part_2():
    line1, line2 = get_input()
    return length_solver(line1, line2)

print(part_2())  # 32132
