from sys import stdin

num_temps = int(stdin.readline())

print(len(list(filter(lambda i: i < 0, map(int, stdin.readline().split(" "))))))
