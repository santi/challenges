from typing import cast
from functools import cmp_to_key

type Cards = tuple[int, int, int, int, int]
type Hand = tuple[Cards, int]


def card_value(card: str, joker_value: int = 11) -> int:
    match card:
        case "A":
            return 14
        case "K":
            return 13
        case "Q":
            return 12
        case "J":
            return joker_value
        case "T":
            return 10
        case _:
            return int(card)


def has_joker(cards: Cards) -> bool:
    return 1 in cards


def num_jokers(cards: Cards) -> int:
    return cards.count(1)


def five_of_a_kind(cards: Cards) -> bool:
    return all(card == cards[0] for card in cards)


def four_of_a_kind(cards: Cards) -> bool:
    return any(cards.count(card) == 4 for card in cards)


def full_house(cards: Cards) -> bool:
    return any(cards.count(card) == 3 for card in cards) and any(
        cards.count(card) == 2 for card in cards
    )


def three_of_a_kind(cards: Cards) -> bool:
    return any(cards.count(card) == 3 for card in cards)


def two_pairs(cards: Cards) -> bool:
    return sum(cards.count(card) == 2 for card in cards) == 4


def one_pair(cards: Cards) -> bool:
    return any(cards.count(card) == 2 for card in cards)


def high_card(cards: Cards) -> bool:
    return all(cards.count(card) == 1 for card in cards)


FIVE_OF_A_KIND = 20
FOUR_OF_A_KIND = 19
FULL_HOUSE = 18
THREE_OF_A_KIND = 17
TWO_PAIRS = 16
ONE_PAIR = 15
HIGH_CARD = 14


def rank(cards: Cards) -> int:
    if five_of_a_kind(cards):
        return FIVE_OF_A_KIND
    elif four_of_a_kind(cards):
        if jokers := num_jokers(cards):
            return FIVE_OF_A_KIND
        else:
            return FOUR_OF_A_KIND
    elif full_house(cards):
        if jokers := num_jokers(cards):
            return FIVE_OF_A_KIND
        else:
            return FULL_HOUSE
    elif three_of_a_kind(cards):
        if jokers := num_jokers(cards):
            if jokers == 1:
                return FOUR_OF_A_KIND
            elif jokers == 2:
                return FIVE_OF_A_KIND
            elif jokers == 3:
                return FOUR_OF_A_KIND
            else:
                raise ValueError("Invalid hand")
        else:
            return THREE_OF_A_KIND
    elif two_pairs(cards):
        if jokers := num_jokers(cards):
            if jokers == 1:
                return FULL_HOUSE
            elif jokers == 2:
                return FOUR_OF_A_KIND
            else:
                raise ValueError("Invalid hand")
        else:
            return TWO_PAIRS
    elif one_pair(cards):
        if jokers := num_jokers(cards):
            if jokers == 1:
                return THREE_OF_A_KIND
            elif jokers == 2:
                return THREE_OF_A_KIND
            else:
                raise ValueError("Invalid hand")
        else:
            return ONE_PAIR
    elif high_card(cards):
        if jokers := num_jokers(cards):
            return ONE_PAIR
        else:
            return HIGH_CARD
    else:
        raise ValueError("Invalid hand")


def compare_hands(hand1: Hand, hand2: Hand) -> int:
    cards1, cards2 = hand1[0], hand2[0]
    if rank(cards1) > rank(cards2):
        return 1
    elif rank(cards1) < rank(cards2):
        return -1
    else:
        if cards1 > cards2:
            return 1
        elif cards1 < cards2:
            return -1
        else:
            return 0


def parse_hand(line: str, joker_value: int = 11) -> Hand:
    cards, bid = line.strip().split(" ")
    hand = cast(
        Hand, (tuple(card_value(card, joker_value=joker_value) for card in cards), int(bid))
    )
    return hand


def main():
    with open("day07/input.txt") as f:
        lines = f.readlines()
        hands: list[Hand] = [parse_hand(line) for line in lines]
        hands.sort(key=cmp_to_key(compare_hands))

        print("Part 1:", sum(hand[1] * (i + 1) for i, hand in enumerate(hands)))

        hands: list[Hand] = [parse_hand(line, joker_value=1) for line in lines]
        hands.sort(key=cmp_to_key(compare_hands))

        print("Part 2:", sum(hand[1] * (i + 1) for i, hand in enumerate(hands)))


if __name__ == "__main__":
    main()
