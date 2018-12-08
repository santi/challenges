__author__ = 'vemund'


with open('luke5', 'r') as f:
    hash = dict()
    for line in f.readlines():
        line = "".join(sorted(line.strip()))
        if hash.get(line):
            hash[line] += 1
        else:
            hash[line] = 1
    n = 0
    for key in hash.keys():
        if hash[key] > 1:
            n += hash[key]
    print(n)