__author__ = 'Vemund'


def sum_threes_and_fives(number):
    result = 0
    for i in range(number):
        if i % 5 == 0:
            result += i
        elif i % 3 == 0:
            result += i
    return result

print(sum_threes_and_fives(1000))
