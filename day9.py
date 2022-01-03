from pathlib import Path

path = Path('input\day9.txt')
problem = Path.read_text(path)
height = problem.strip().split('\n')

# Part 1:
heightmap = []
for h in height:
    hm = []
    for c in h:
        hm.append(int(c))
    heightmap.append(hm)

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

low_points = []
coordinates = []
for i, row in enumerate(heightmap):
    row_length = len(row)
    for j, col in enumerate(row):
        neighbors, coor = get_neighbors(heightmap, i, j)
        if col < min(neighbors):
            low_points.append(col)
            coordinates.append((i, j))

print(sum(low_points) + len(low_points))

# Part 2:
basins = []
for i, coor in enumerate(coordinates):
    basin_coor = [coor]
    j = 0
    unclosed = True
    while unclosed:
        neighbors, coor = get_neighbors(heightmap, basin_coor[j][0], basin_coor[j][1])
        for n, c in zip(neighbors, coor):
            if n < 9 and c not in basin_coor:
                basin_coor.append(c)
        if j == len(basin_coor) - 1:
            break
        j += 1
    basins.append(len(basin_coor))

sizes = sorted(basins, reverse = True)[:3]
print(sizes[0] * sizes[1] * sizes[2])