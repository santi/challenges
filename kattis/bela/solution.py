from sys import stdin

hands, dominant = stdin.readline().strip().split(" ")
hands = int(hands)

CARD_VALUES = {
    'A': [11, 11],
    'K': [4, 4],
    'Q': [3, 3],
    'J': [20, 2],
    'T': [10, 10],
    '9': [14, 0],
}

def get_value(card, dominant):
    number, suit = list(card)
    value = CARD_VALUES.get(number, [0, 0])
    return value[0] if suit == dominant else value[1]


total_points = 0
for card in range(4 * hands):
    total_points += get_value(stdin.readline().strip(), dominant)
print(total_points)
