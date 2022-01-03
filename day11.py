from pathlib import Path
import numpy as np

path = Path('input\day11.txt')
problem = Path.read_text(path)
octopuses = problem.strip().split('\n')

for i, l in enumerate(octopuses):
    line = []
    for c in l:
        line.append(int(c))
    octopuses[i] = line

array = np.array(octopuses)

def get_neighbors(row, col):
    neighbors = {(row - 1, col), (row - 1, col + 1), (row, col + 1), (row + 1, col + 1), (row + 1, col), (row + 1, col - 1), (row, col - 1), (row - 1, col -1)}
    valid_neighbors = set()
    for pos in neighbors:
        if (pos[0] < 0) or (pos[0] > 9) or (pos[1] < 0) or (pos[1] > 9):
            continue
        valid_neighbors.add(pos)
    return valid_neighbors

def flash(array):
    flashed_coor = set()
    array += 1
    unflashed = True
    flashes = 0
    while unflashed:
        new_flashes = 0
        for i, row in enumerate(array):
            for j, col in enumerate(row):
                if (i, j) in flashed_coor:
                    continue
                if col > 9:
                    new_flashes += 1
                    flashed_coor.add((i, j))
                    neighbors = get_neighbors(i, j)
                    for pos in neighbors:
                        array[pos[0]][pos[1]] += 1
        if new_flashes == 0:
            unflashed = False
        flashes += new_flashes

    for i, row in enumerate(array):
        for j, col in enumerate(row):
            if col > 9:
                array[i][j] = 0

    return(array, flashes)

copy_array = np.copy(array)

# Part 1:
total_flashes = 0
for i in range(100):
    array, flashes = flash(array)
    total_flashes += flashes
print(total_flashes)

# Part 2:
step = 0
flashes = 0
while flashes != 100:
    step += 1
    copy_array, flashes = flash(copy_array)
print(step)

