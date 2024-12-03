import re

mul_matcher = "mul\\(([0-9]{1,3}),([0-9]{1,3})\\)"
advanced_mul_matcher = re.compile(f"{mul_matcher}|(do\\(\\))|(don\'t\\(\\))")

def main():
    with open("day03/input.txt") as f:
        instructions = "".join(f.readlines())

    matches = re.findall(mul_matcher, instructions)
    print("Part 1:", sum(map(lambda match: int(match[0]) * int(match[1]), matches)))



    matches = advanced_mul_matcher.findall(instructions)

    result = 0
    machine_enabled = True
    for match in matches:
        if match[2]:
            machine_enabled = True
        elif match[3]:
            machine_enabled = False
        elif machine_enabled:
            result += int(match[0]) * int(match[1])

    print("Part 2:", result)

    
if __name__ == "__main__":
    main()
