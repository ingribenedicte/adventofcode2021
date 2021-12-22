from pathlib import Path
import numpy as np

path = Path('input\day9.txt')
problem = Path.read_text(path)
height = problem.strip().split('\n')

heightmap = []
for h in height:
    hm = []
    for c in h:
        hm.append(int(c))
    heightmap.append(hm)
heightmap = np.array(heightmap)
print(heightmap)

def get_neighbors(map, i, j):
    coordinates = []
    neighbors = []
    n = len(map) - 1
    m = len(map[0]) - 1
    if i != 0 and i != n:
        neighbors.append(map[i - 1][j])
        neighbors.append(map[i + 1][j])
        coordinates.append((i - 1, j))
        coordinates.append((i + 1, j))
    if i == 0:
        neighbors.append(map[i + 1][j])
        coordinates.append((i + 1, j))
    if i == n:
        neighbors.append(map[i - 1][j])
        coordinates.append((i - 1, j))
    if j != 0 and j != m:
        neighbors.append(map[i][j - 1])
        neighbors.append(map[i][j + 1])
        coordinates.append((i, j - 1))
        coordinates.append((i, j + 1))
    if j == 0:
        neighbors.append(map[i][j + 1])
        coordinates.append((i, j + 1))
    if j == m:
        neighbors.append(map[i][j - 1])
        coordinates.append((i, j - 1))
    return neighbors, coordinates

def get_basin_neighbors(map, i, j):
    coordinates = []
    neighbors = []
    n = len(map) - 1
    m = len(map[0]) - 1
    if i != 0 and i != n:
        neighbors.append(map[i - 1][j])
        neighbors.append(map[i + 1][j])
        coordinates.append((i - 1, j))
        coordinates.append((i + 1, j))
    if i == 0:
        neighbors.append(map[i + 1][j])
        coordinates.append((i + 1, j))
    if i == n:
        neighbors.append(map[i - 1][j])
        coordinates.append((i - 1, j))
    if j != 0 and j != m:
        neighbors.append(map[i][j - 1])
        neighbors.append(map[i][j + 1])
        coordinates.append((i, j - 1))
        coordinates.append((i, j + 1))
    if j == 0:
        neighbors.append(map[i][j + 1])
        coordinates.append((i, j + 1))
    if j == m:
        neighbors.append(map[i][j - 1])
        coordinates.append((i, j - 1))

    basin_neighbors = []
    basin_coordinates = []
    for k, bn in enumerate(neighbors):
        if bn != 9:
            basin_neighbors.append(bn)
            basin_coordinates.append(coordinates[k])
    return basin_neighbors, basin_coordinates

low_points = []
coordinates = []
for i, row in enumerate(heightmap):
    row_length = len(row)
    for j, col in enumerate(row):
        neighbors, coor = get_neighbors(heightmap, i, j)

        if col < min(neighbors):
            low_points.append(col)
            coordinates.append((i, j))

print(low_points, coordinates)

basins = []
for coordinate in coordinates:
    i = coordinate[0]
    j = coordinate[1]
    basin = []
    basin.append(heightmap[i][j])
    coor_set = set()

    undiscovered = True
    while undiscovered:
        neighbors, coor = get_basin_neighbors(heightmap, i, j)
        coor = set(coor)
        if len(neighbors) == 0:
            undiscovered = False
        basin.extend(neighbors)
        coor_set = coor_set.union(coor)

    basins.append(len(basin))