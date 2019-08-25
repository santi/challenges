inp = [[4, 2, 11], [6, 5, 4], [-12, 8, 10]]



def diag(a):
    entries = []
    for i in range(len(a)):
        entries.append(a[i][i])
    return entries

def reverse(a):
    b = []
    for i in range(len(a)):
        b.append(a[i][::-1])
    return a

def n_sum(a):
    if type(a) is int:
        return a
    elif len(a) == 0:
        return 0
    else:
        return n_sum(a[0]) + n_sum(a[1:])


def diagonalDifference(a):
    sum1 = n_sum(diag(a))
    return abs(sum1) - n_sum(diag(reverse(a)))

print(diagonalDifference(inp))
