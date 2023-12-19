from functools import lru_cache


def get_next_record(conditions: str, current_damage_group: int) -> str:
    if current_damage_group >= len(conditions):
        return "."
    else:
        return conditions[current_damage_group]


def is_valid_damage_group(conditions: str, damage_group: int) -> bool:
    records = conditions[:damage_group]
    next_record = get_next_record(conditions, damage_group)
    return (
        len(records) == damage_group
        and all([condition in {"#", "?"} for condition in records])
        and next_record in {".", "?"}
    )


@lru_cache()
def get_combinations(conditions: str, damage_groups: list[int]) -> int:
    #  Termination condition. No more records
    if conditions == "":
        if len(damage_groups) == 0:
            return 1
        else:
            return 0

    #  Termination condition. No more groups
    if len(damage_groups) == 0:
        if any([condition == "#" for condition in conditions]):
            return 0
        else:
            return 1

    # Record is a working spring. Just continue
    if conditions[0] == ".":
        return get_combinations(conditions[1:], damage_groups)

    # Record is a broken spring. This spring must be included in the next damage group
    elif conditions[0] == "#":
        damage_group = damage_groups[0]
        if is_valid_damage_group(conditions, damage_group):
            return get_combinations(conditions[damage_group + 1 :], damage_groups[1:])
        else:
            return 0

    # Record is unknown. This spring can be included in the next damage group or not
    elif conditions[0] == "?":
        damage_group = damage_groups[0]
        if is_valid_damage_group(conditions, damage_group):
            return get_combinations(
                conditions[damage_group + 1 :], damage_groups[1:]
            ) + get_combinations(conditions[1:], damage_groups)
        else:
            return get_combinations(conditions[1:], damage_groups)

    # This condition should never be met
    else:
        raise ValueError("Invalid condition", conditions, damage_groups)


def parse_history(lines: list[str], duplication_factor=1) -> list[tuple[str, tuple[int, ...]]]:
    history: list[tuple[str, tuple[int, ...]]] = []
    for line in lines:
        records, damage_groups = line.strip().split(" ")
        history.append(
            (
                ((records + "?") * duplication_factor)[:-1],
                tuple(
                    int(damage_group)
                    for damage_group in (((damage_groups + ",") * duplication_factor)[:-1]).split(
                        ","
                    )
                ),
            )
        )
    return history


def main():
    with open("day12/input.txt") as f:
        lines = f.readlines()

        print("Part 1:", sum(get_combinations(*history) for history in parse_history(lines)))
        print("Part 2:", sum(get_combinations(*history) for history in parse_history(lines, 5)))


if __name__ == "__main__":
    main()
