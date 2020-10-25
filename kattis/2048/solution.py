from sys import stdin

LEFT = "LEFT"
UP = "UP"
RIGHT = "RIGHT"
DOWN = "DOWN"

DIRECTION = {
    0: LEFT,
    1: UP,
    2: RIGHT,
    3: DOWN
}


def print_output(board):
    for line in board:
        print(" ".join(map(str,line)))


class Cell:
    def __init__(self, value):
        self.value = int(value)
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return str(self.value)

    def can_merge(self, other):
        return self.value != 0 and self.value == other.value
    
    def merge(self, other):
        return Cell(self.value + other.value)


board = list(map(lambda line: list(map(Cell, line.strip().split())), [
    stdin.readline() for i in range(4)
]))

direction = DIRECTION[int(stdin.readline())]

def get_row(board, i):
    return board[i]

def get_col(board, i):
    return [board[j][i] for j in range(4)]

def board_to_seq(board, direction):
    if direction == LEFT:
        return [get_row(board, i) for i in range(4)]
    elif direction == UP:
        return [get_col(board, i) for i in range(4)]
    elif direction == RIGHT:
        return [get_row(board, i)[::-1] for i in range(4)]
    elif direction == DOWN:
        return [get_col(board, i)[::-1] for i in range(4)]
    else:
        raise RuntimeError("Unsupported direction: " + direction)


def seq_to_board(sequences, direction):
    if direction == DOWN:
        return [*reversed(board_to_seq(sequences, UP))]
    return board_to_seq(sequences, direction)


def move(sequence):
    sequence = list(filter(lambda cell: cell.value != 0, sequence))
    pos = 0
    new_seq = []
    while pos < len(sequence):
        if pos == len(sequence) - 1:
            new_seq.append(sequence[pos])
            break
        cell1, cell2 = sequence[pos], sequence[pos + 1]
        if cell1.can_merge(cell2):
            new_seq.append(cell1.merge(cell2))
            pos += 2
        else:
            new_seq.append(cell1)
            pos += 1
    [new_seq.append(Cell(0)) for i in range(4 - len(new_seq))]
    return new_seq


def solve(board, direction):
    sequences = board_to_seq(board, direction)
    merged_sequences = []
    for sequence in sequences:
        merged_sequences.append(move(sequence))
    return seq_to_board(merged_sequences, direction)


print_output(solve(board, direction))

