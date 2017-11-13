import re

__author__ = 'vemund'


def is_turnable(n):
    return re.match(r'[01689]*$', n)


def turn(n):
    n = str(n[::-1])
    for i in range(len(n)):
        if n[i] == '9':
            n = n[:i] + '6' + n[i + 1:]
        elif n[i] == '6':
            n = n[:i] + '9' + n[i + 1:]
    print 'Turned:' + n
    return n

count = 0
for i in range(100001):
    n = str(i)
    if is_turnable(n):
        if n == turn(n):
            print n + ' er lik ' + turn(n)
            count += 1
print count
