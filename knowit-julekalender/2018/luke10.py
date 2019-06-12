
with open('luke10.txt') as f:
    program = f.readlines()

machine = []
for line in program:
    for command in line:
        if command == ':':
            machine = [sum(machine)]

        elif command == '|':
            machine.append(3)

        elif command == "'":
            a = machine.pop()
            b = machine.pop()
            machine.append(a + b)

        elif command == '.':
            a = machine.pop()
            b = machine.pop()
            machine.append(a - b)
            machine.append(b - a)

        elif command == '_':
            a = machine.pop()
            b = machine.pop()
            machine.append(a * b)
            machine.append(a)

        elif command == '/':
            machine.pop()

        elif command == 'i':
            a = machine.pop()
            machine.append(a)
            machine.append(a)

        elif command == '\\':
            a = machine.pop()
            machine.append(a + 1)

        elif command == '*':
            a =  machine.pop()
            b = machine.pop()
            machine.append(a//b)

        elif command == ']':
            a = machine.pop()
            if a % 2 == 0:
                machine.append(1)

        elif command == '[':
            a = machine.pop()
            if a % 2 == 1:
                machine.append(a)

        elif command == '~':
            a = machine.pop()
            b = machine.pop()
            c = machine.pop()
            machine.append(max(a, b, c))

        elif command == 'K':
            break

        elif command == ' ':
            machine.append(31)

        elif command == '\n':
            pass

        else:
            print(command)
            raise ValueError(f'Invalid operand: {command}')

print(max(machine))
