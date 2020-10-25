from sys import stdin

def fizz_buzz(number, X, Y):
    output = ""
    if number % X == 0:
        output += "Fizz"
    if number % Y == 0:
        output += "Buzz"
    return str(number) if output == "" else output

X, Y, N = map(int, stdin.readline().strip().split(" "))
for num in range(1, N + 1):
    print(fizz_buzz(num, X, Y))