import re
from operator import gt, lt
from typing import Callable, Literal


type Category = Literal["x", "m", "a", "s"]
type Part = dict[Category, int]
type Predicate = Callable[[Part], bool]
type Rule = tuple[Predicate, str, str]
type Workflow = list[Rule]


def get_parts(lines: list[str]) -> list[Part]:
    x = "x"
    m = "m"
    a = "a"
    s = "s"

    parts: list[Part] = []
    for _ in range(len(lines)):
        line = lines.pop()
        if line.strip() == "":
            break
        parts.append(eval(line.replace("=", ":")))
    return parts


def parse_predicate(predicate: str) -> tuple[Category, str, int]:
    return (predicate[0], predicate[1], int(predicate[2:]))


def get_predicate(predicate: str) -> Predicate:
    property, operator, value = parse_predicate(predicate)
    operator_fn = gt if ">" == operator else lt

    def f(part: Part) -> bool:
        return operator_fn(part[property], value)

    return f


def get_rule(instruction: str) -> Rule:
    parts = instruction.split(":")
    if len(parts) == 1:

        def f(part: Part) -> bool:
            return True

        return (f, parts[0], instruction)

    predicate, destination = parts
    return (get_predicate(predicate), destination, instruction)


def get_workflows(lines: list[str]) -> dict[str, Workflow]:
    workflow_pattern = re.compile(r"(\w+)\{(.*)\}")
    workflows = {}
    for line in lines:
        workflow_name, instructions = workflow_pattern.match(line).groups()
        instructions = [get_rule(instruction) for instruction in instructions.split(",")]

        workflows[workflow_name] = instructions

    return workflows


def is_accepted(workflows: dict[str, Workflow], workflow_name: str, part: Part) -> bool:
    workflow = workflows[workflow_name]
    for rule in workflow:
        predicate, destination, _ = rule
        if predicate(part):
            if destination == "A":
                return True
            elif destination == "R":
                return False
            else:
                return is_accepted(workflows, destination, part)


def part_value(part: Part) -> int:
    return sum(part.values())


def part_combinations(limits: dict[Category, tuple[int, int]]) -> int:
    return (
        (limits["x"][1] - limits["x"][0] + 1)
        * (limits["m"][1] - limits["m"][0] + 1)
        * (limits["a"][1] - limits["a"][0] + 1)
        * (limits["s"][1] - limits["s"][0] + 1)
    )


def get_valid_combinations(
    workflows: dict[str, Workflow],
    workflow: Workflow,
    limits: dict[Category, tuple[int, int]],
) -> int:
    _, _, instruction = workflow[0]
    if instruction == "A":
        return part_combinations(limits)
    elif instruction == "R":
        return 0

    parts = instruction.split(":")
    if len(parts) == 1:
        return get_valid_combinations(workflows, workflows[instruction], limits)

    predicate, destination = parts
    property, operator, value = parse_predicate(predicate)
    current_limits: dict[Category, tuple[int, int]] = {**limits}
    next_limits: dict[Category, tuple[int, int]] = {**limits}
    if operator == ">":
        current_limits[property] = (
            max(current_limits[property][0], value + 1),
            current_limits[property][1],
        )
        next_limits[property] = (
            next_limits[property][0],
            min(next_limits[property][1], value),
        )
    elif operator == "<":
        current_limits[property] = (
            current_limits[property][0],
            min(current_limits[property][1], value - 1),
        )
        next_limits[property] = (
            max(next_limits[property][0], value),
            next_limits[property][1],
        )
    else:
        raise ValueError("Invalid operator")

    if destination == "A":
        return part_combinations(current_limits) + get_valid_combinations(
            workflows, workflow[1:], next_limits
        )
    elif destination == "R":
        return get_valid_combinations(workflows, workflow[1:], next_limits)
    else:
        return get_valid_combinations(
            workflows, workflows[destination], current_limits
        ) + get_valid_combinations(workflows, workflow[1:], next_limits)


def main():
    with open("day19/input.txt") as f:
        lines = f.readlines()
    parts = get_parts(lines)
    workflows = get_workflows(lines)

    print("Part 1:", sum(part_value(part) for part in parts if is_accepted(workflows, "in", part)))

    limits: dict[Category, tuple[int, int]] = {
        "x": (1, 4000),
        "m": (1, 4000),
        "a": (1, 4000),
        "s": (1, 4000),
    }
    print(
        "Part 2:",
        get_valid_combinations(workflows, workflows["in"], limits),
    )


if __name__ == "__main__":
    main()
