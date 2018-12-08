__author__ = 'Vemund'

def indexOf():
    from sys import stdin
    from collections import Counter

    group_size = int(stdin.readline())
    die_rolls = stdin.readline().split()

    valueNums = [0]*6
    valueIndex = [None]*6


    for i in range(group_size):
        valueNums[int(die_rolls[i]) - 1] += 1
        valueIndex[int(die_rolls[i]) - 1] = i
    valueNums = valueNums[::-1]
    valueIndex = valueIndex[::-1]
    for index, value in enumerate(valueNums):
        if value == 1:
            return valueIndex[index] + 1
    return 'none'

def main():
    print(indexOf())


main()
