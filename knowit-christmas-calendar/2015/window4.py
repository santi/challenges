__author__ = 'vemund'

with open('luke4', 'r') as f:
    text = "".join(f.readlines())
    count = [0,0,0,0]
    for c in text:
        if c == 'A':
            count[0] += 1
        elif c == 'C':
            count[1] += 1
        elif c == 'G':
            count[2] += 1
        elif c == 'T':
            count[3] += 1
    print count