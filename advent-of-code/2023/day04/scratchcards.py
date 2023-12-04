from collections import defaultdict


def get_numbers(card: str) -> tuple[set[int], set[int]]:
    winner_part, your_part = card.strip().replace("  ", " ").split("|")
    _, winner_number_row = winner_part.strip().split(":")
    winner_numbers = set(int(number) for number in winner_number_row.strip().split(" "))
    your_numbers = set(int(number) for number in your_part.strip().split(" "))

    return winner_numbers, your_numbers


def get_number_of_matches(cards: list[str]) -> int:
    card_points = 0
    for card in cards:
        winner_numbers, your_numbers = get_numbers(card)
        matches = winner_numbers.intersection(your_numbers)
        card_points += 2 ** (len(matches) - 1) if matches else 0
    return card_points


def get_total_number_of_cards(cards: list[str]) -> int:
    card_multipliers = defaultdict(lambda: 1)
    for card_no, line in enumerate(cards):
        winner_numbers, your_numbers = get_numbers(line)
        matches = winner_numbers.intersection(your_numbers)
        for next_card_no in range(1, len(matches) + 1):
            card_multipliers[card_no + next_card_no] += card_multipliers[card_no]
    return sum(card_multipliers.values())


with open("day04/input.txt") as f:
    lines = f.readlines()

    print("Part 1:", get_number_of_matches(lines))
    print("Part 2:", get_total_number_of_cards(lines))
