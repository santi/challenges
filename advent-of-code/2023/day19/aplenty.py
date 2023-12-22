import re
from operator import gt, lt
from typing import Callable, Literal


type Category = Literal["x", "m", "a", "s"]
type Part = dict[Category, int]
type Predicate = Callable[[Part], bool]
type Rule = tuple[Predicate, str]


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


def get_predicate(predicate: str) -> Predicate:
    operator = gt if ">" == predicate[1] else lt
    property: Category = predicate[0]
    value = int(predicate[2:])

    def f(part: Part) -> bool:
        return operator(part[property], value)

    return f


def get_rule(instruction: str) -> Rule:
    parts = instruction.split(":")
    if len(parts) == 1:

        def f(part: Part) -> bool:
            return True

        return (f, parts[0])

    predicate, destination = parts
    return (get_predicate(predicate), destination)


def get_workflows(lines: list[str]) -> dict[str, list[Rule]]:
    workflow_pattern = re.compile(r"(\w+)\{(.*)\}")
    workflows = {}
    for line in lines:
        workflow_name, instructions = workflow_pattern.match(line).groups()
        instructions = [get_rule(instruction) for instruction in instructions.split(",")]

        workflows[workflow_name] = instructions

    return workflows


def run_workflow(workflows: dict[str, list[Rule]], workflow_name: str, part: Part) -> bool:
    workflow = workflows[workflow_name]
    for rule in workflow:
        predicate, destination = rule
        if predicate(part):
            if destination == "A":
                return True
            elif destination == "R":
                return False
            else:
                return run_workflow(workflows, destination, part)


def part_value(part: Part) -> int:
    return sum(part.values())


def main():
    with open("day19/input.txt") as f:
        lines = f.readlines()
    parts = get_parts(lines)
    workflows = get_workflows(lines)

    print("Part 1:", sum(part_value(part) for part in parts if run_workflow(workflows, "in", part)))


if __name__ == "__main__":
    main()
