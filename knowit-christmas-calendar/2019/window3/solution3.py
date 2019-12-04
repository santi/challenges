import requests
import math


def get_input():
    return requests.get("https://knowit-julekalender.s3.eu-central-1.amazonaws.com/2019-luke3/img.txt").text


def solve(image):
    length = 1287
    with open("window3/output.txt", "w") as f:
        for i in range(0, len(image), length):
            print(image[i:i + length])
            f.write(image[i:i + length] + "\n")



print(solve(get_input()))
