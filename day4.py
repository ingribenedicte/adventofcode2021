from pathlib import Path
from collections import Counter

path = Path('input\day4.txt')
problem = Path.read_text(path)
bingo = problem.split('\n')

numbers = bingo[0].split(',')
bingo = bingo[2:]

boards = []
board = []
for b in bingo:
    if b == '':
        boards.append(board)
        board = []
    else:
        b = b.split()
        board.append(b)

def win(pos):
    if len(pos) == 0:
        return False

    row, col = zip(*pos)

    r = Counter(row)
    r_max = r.most_common(1)

    c = Counter(col)
    c_max = c.most_common(1)

    return r_max[0][1] == 5 or c_max[0][1] == 5

def score(board, positions, number):
    anws = 0
    for i, r in enumerate(board):
        for j, c in enumerate(r):
            pos = (i, j)
            if not pos in positions:
                anws += int(c)
    return anws * number

# Part 1:
pos = [list() for _ in range(len(boards))]
done = False
for number in numbers:
    if done:
        break
    for n, board in enumerate(boards):
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if number == col:
                    tuple = (i, j)
                    pos[n].append(tuple)
                    if win(pos[n]):
                        winner_board = board
                        winner_positions = pos[n]
                        winner_number = number
                        done = True

print(score(winner_board, winner_positions, int(winner_number)))

# Part 2:
pos = [list() for _ in range(len(boards))]
done = False
winning = set()
for number in numbers:
    if done:
        break
    for n, board in enumerate(boards):
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if number == col:
                    tuple = (i, j)
                    pos[n].append(tuple)
                    if win(pos[n]):
                        winning.add(n)
        if len(winning) == len(boards):
            loser_board = board
            loser_positions = pos[n]
            loser_number = number
            done = True
            break

print(score(loser_board, loser_positions, int(loser_number)))