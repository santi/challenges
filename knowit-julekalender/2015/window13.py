__author__ = 'vemund'


def isUgly(num):
    if num == 0:
        return False
    for i in [2, 3, 5]:
        while num % i == 0:
            num /= i
    return num == 1

count = 0
tall = 0
while count < 10000:
    if isUgly(tall):
        count += 1
        print str(tall), 'er knalltall', count
    tall += 1
