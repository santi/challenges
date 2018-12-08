
def main():
    from sys import stdin
    longSides = {}
    lEven = 0.5946035575
    lOdd = 0.4204482076
    smallest_paper_size = int(stdin.readline())
    a1_size = 2**30
    paper_sizes = [0] + stdin.readline().split()
    print(paper_sizes)
    covered = 0
    for size, paper in enumerate(paper_sizes):
        covered += int(paper)*2**(30-size)
    if covered < a1_size:
        return 'impossible'




    print('Size of A1:', a1_size)
    print('Size of covered:', covered)
main()