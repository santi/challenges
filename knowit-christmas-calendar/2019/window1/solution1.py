#!/usr/bin/env python3
import requests
import sys
sys.setrecursionlimit(10000)


def get_input():
    sheep = requests.get('https://knowit-julekalender.s3.eu-central-1.amazonaws.com/sau.txt').text
    sheep = list(map(int, sheep.split(', ')))
    return sheep


def survival_days(sheep_counts, dragon_size, leftover_sheep, days_hungry, survived_days):
    if days_hungry == 5:
        return survived_days - 1  # survived_days has increased since last function invocation
    
    num_sheep = sheep_counts[0]
    if leftover_sheep + num_sheep >= dragon_size:
        return survival_days(
            sheep_counts[1:],
            dragon_size + 1,
            leftover_sheep + num_sheep - dragon_size,
            0,
            survived_days + 1)
    else:
        return survival_days(
            sheep_counts[1:],
            dragon_size - 1,
            0,
            days_hungry + 1,
            survived_days + 1)

print(survival_days(get_input(), 50, 0, 0, 0))
        
        
        


