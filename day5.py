from pathlib import Path

path = Path('input\day5.txt')
problem = Path.read_text(path)
lines = problem.split('\n')

coordinates = []
for l in lines:
    l = l.split(' -> ')
    l = [y.split(',') for y in l]
    coordinates.append(l)

points = set()
points_overlap = set()
for c in coordinates:
    x_1 = int(c[0][0])
    x_2 = int(c[1][0])
    y_1 = int(c[0][1])
    y_2 = int(c[1][1])

    if x_1 == x_2:
        y_coor = list(range(min(y_1, y_2), max(y_1, y_2) + 1))
        x_coor = [x_1] * len(y_coor)

    elif y_1 == y_2:
        x_coor = list(range(min(x_1, x_2), max(x_1, x_2) + 1))
        y_coor = [y_1] * len(x_coor)

    # Include diagonal lines:
    else:
        if x_1 < x_2:
            x_coor = list(range(x_1, x_2 + 1))
        if x_1 > x_2:
            x_coor = list(range(x_1, x_2 - 1, -1))
        if y_1 < y_2:
            y_coor = list(range(y_1, y_2 + 1))
        if y_1 > y_2:
            y_coor = list(range(y_1, y_2 - 1, -1))

    for x, y in zip(x_coor, y_coor):
        point = (x, y)
        if point in points:
            points_overlap.add(point)
        points.add(point)

print(len(points_overlap))