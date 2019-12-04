import requests
import sys
sys.setrecursionlimit(10000)


def get_input():
    raw_coordinates = requests.get("https://knowit-julekalender.s3.eu-central-1.amazonaws.com/2019-luke4/coords.csv").text.split("\n")
    coordinates = []
    for line in raw_coordinates[1:-1]:
        coordinate = line.split(",")
        coordinates.append((int(coordinate[0]), int(coordinate[1])))
    return coordinates


def walk_x(_from, _to, y, time_spent, visited):
    if _from == _to:
        return time_spent

    position = (_from, y)

    time_spent += visited.get(position, 1)
    visited[position] = visited.get(position, 1) + 1
    
    direction = 1 if _from < _to else -1
    return walk_x(_from + direction, _to, y, time_spent, visited)


def walk_y(_from, _to, x, time_spent, visited):
    if _from == _to:
        return time_spent

    position = (x, _from)

    time_spent += visited.get(position, 1)
    visited[position] = visited.get(position, 1) + 1
    
    direction = 1 if _from < _to else -1
    return walk_y(_from + direction, _to, x, time_spent, visited)


def walk(coordinates, current_x, current_y, time_spent, visited):
    if not coordinates:
        return time_spent

    next_x, next_y = coordinates[0]

    time_spent = walk_x(current_x, next_x, current_y, time_spent, visited)
    time_spent = walk_y(current_y, next_y, next_x, time_spent, visited)

    return walk(coordinates[1:], next_x, next_y, time_spent, visited)


coordinates = get_input()  # [(1, 3), (1, 0), (3, 2)]

print(walk(coordinates, 0, 0, 0, dict()))  # 394426
