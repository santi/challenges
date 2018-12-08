
def main():
    from sys import stdin
    longSides = {}
    short_side = 0.42044820762685727151556273811661
    long_side = 0.59460355750136053335874998528024
    smallest_paper_size = int(stdin.readline())
    a1_size = 2**30
    paper_sizes = [0] + stdin.readline().split()
    print(paper_sizes)
    covered = 0
    tape= 0
    for size, paper in enumerate(paper_sizes):
        tape += long_side**(-2*size)
        covered += int(paper)*2**(30-size)
    if covered < a1_size:
        return 'impossible'



    print('Tape used:', tape)
    print('Size of A1:', a1_size)
    print('Size of covered:', covered)
main()