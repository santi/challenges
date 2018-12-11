with open('luke11.txt') as f:
    path = f.readlines()[0].strip()


index = 0
number = ''
coordinate = (0, 0)

while index < len(path):
    if path[index] == 'H':
        steps = int(number)
        coordinate = (coordinate[0] + steps, coordinate[1])
        number = ''

    elif path[index] == 'V':
        steps = int(number)
        coordinate = (coordinate[0] - steps, coordinate[1])
        number = ''

    elif path[index] == 'F':
        steps = int(number)
        coordinate = (coordinate[0], coordinate[1] + steps)
        number = ''

    elif path[index] == 'B':
        steps = int(number)
        coordinate = (coordinate[0], coordinate[1] - steps)
        number = ''

    else:
        number += path[index]

    index += 1

print(f'[{coordinate[0]},{coordinate[1]}]')
