from collections import deque


start = "sand"
end = "hold"


def format(n):
    return n.lower().strip()

data = open("luke21").readlines()
for i in range(len(data)):
    data[i] = format(data[i])

stakk = deque()
stakk.appendleft((start, 1))
visited = set()
current = ""
while current != end:
    current, depth = stakk.pop()
    if end == current:
        print("Bingo!", current[1])
    if current in visited or len(current) > 4:
        continue
    visited.add(current)

    for node in data:
        matches = 0
        for i in range(len(node)):
            if node[i] == current[i]:
                matches += 1
        if matches == 3:
            stakk.appendleft((node, depth + 1))