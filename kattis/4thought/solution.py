from sys import stdin

test_cases = int(stdin.readline())

def enumerate_fours(expr, possible_values, fours_left):
    if fours_left == 0:
        answer = eval(expr)
        possible_values[answer] = expr.replace("//", "/") + " = " + str(answer)
        return possible_values
    for operator in [" + ", " - ", " // ", " * "]:
        enumerate_fours(expr + operator + "4", possible_values, fours_left - 1)

possible_values = {}
enumerate_fours("4", possible_values, 3)

for i in range(test_cases):
    inp = int(stdin.readline())

    if possible_values.get(inp):
        print(possible_values.get(inp))
    else:
        print("no solution")
    
