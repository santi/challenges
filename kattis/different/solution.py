from sys import stdin


for line in stdin:
    a, b = line.strip().split(" ")
    a, b = int(a), int(b)
    print(abs(a - b))
