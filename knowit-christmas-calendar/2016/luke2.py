
first = 0
second = 1
sum_even_fibs = 0
while first + second < 4000000000:
    temp = first
    first = second
    second = temp + second
    print(second)
    if second % 2 == 0:
        sum_even_fibs += second
print(sum_even_fibs)
