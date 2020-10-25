from sys import stdin

test_cases = int(stdin.readline())
for test in range(test_cases):
    visited_cities = set()
    cities = int(stdin.readline())
    for city in range(cities):
        visited_cities.add(stdin.readline())
    print(len(visited_cities))
