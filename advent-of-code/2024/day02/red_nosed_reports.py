from typing import Generator

def one_removed(report: list[int]) -> Generator[list[int]]:
    for v in range(len(report)):
        yield report[:v] + report[v+1:]

def is_bounded_increasing(diff: list[int]) -> bool:
    return all(map(lambda v: (0 < v <= 3), diff))

def is_bounded_decreasing(diff: list[int]) -> bool:
    return all(map(lambda v: (0 > v >= -3), diff))

def is_safe_report(report: list[int]) -> bool:
    diff = [a - b for a, b in zip(report, report[1:])]
    return is_bounded_increasing(diff) or is_bounded_decreasing(diff)

def is_tolerated_report(report: list[int]) -> bool:
    return is_safe_report(report) or any(is_safe_report(rep) for rep in one_removed(report))
    
    

def main():
    with open("day02/input.txt") as f:
        lines = f.readlines()
    reports = list(map(lambda s: list(map(int, s.strip().split(" "))), lines))

    print("Part 1: ", sum(is_safe_report(report) for report in reports))
    print("Part 2: ", sum(is_tolerated_report(report) for report in reports))
    
if __name__ == "__main__":
    main()
