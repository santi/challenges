from collections import defaultdict

def main():
    with open("day01/input.txt") as f:
        lines = f.readlines()
    
    first: list[int] = []
    second: list[int] = []
    for line in lines:
        f, s = line.split("   ")
        first.append(int(f))
        second.append(int(s))
    first = sorted(first)
    second = sorted(second)
    
    total_distance = 0
    for f, s in zip(first, second):
        value = abs(f - s)
        total_distance += value
    print("Part 1:", total_distance)

    frequencies = defaultdict(int)
    for s in second:
        frequencies[s] += 1 
    similarity_score = [f * frequencies[f] for f in first]
    print("Part 2:", sum(similarity_score))

if __name__ == "__main__":
    main()
