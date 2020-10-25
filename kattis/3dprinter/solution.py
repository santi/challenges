from sys import stdin
from math import log2, ceil

inp = int(stdin.readline())

print(int(ceil(log2(inp) + 1)))
