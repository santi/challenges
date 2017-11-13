solved = False
count = 1
while not solved:
    if str(count)[-1] == '6':
        times_four = count * 4
        num_str = str(count)
        print(num_str)
        num_str = num_str[-1] + num_str[:-1]
        if int(num_str) == times_four:
            solved = True
            break
    count += 1
print(count)
