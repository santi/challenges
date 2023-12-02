from operator import mul
from typing import Literal
from functools import reduce
from collections import defaultdict

type Color = Literal["red"] | Literal["green"] | Literal["blue"]

def get_game_id(game_meta: str) -> int:
    return int(game_meta.split(" ")[1])

def get_counts(draws: list[str]) -> dict[Color, int]:
    counts = defaultdict(int)
    for round in draws:
        colors = round.split(",")
        for color in colors:
            number, color = color.strip().split(" ")
            counts[color] = max(counts[color], int(number))
    return counts


def game_value(game: str) -> int:
    game_meta, draws = game.split(':')
    game_id = get_game_id(game_meta)
    counts = get_counts(draws.split(";"))

    if counts["red"] > 12 or counts["green"] > 13 or counts["blue"] > 14:
        return 0

    return game_id

def game_power(game: str) -> int:
    _, draws = game.split(':')
    counts = get_counts(draws.split(";"))

    return reduce(mul, counts.values())

with open('input.txt') as f:
    games = f.readlines()
    print("Part 1:", sum(game_value(game) for game in games))
    print("Part 2:", sum(game_power(game) for game in games))

        
                    
