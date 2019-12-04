import requests


def get_input():
    return requests.get("https://knowit-julekalender.s3.eu-central-1.amazonaws.com/2019-luke2/world.txt").text.split("\n")


def solve(world, acc):
    if not world:
        return acc
    else:
        return solve(world[1:], acc + world[0].strip().count(" "))


print(solve(get_input(), 0))
