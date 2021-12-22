from pathlib import Path

path = Path('input\day7.txt')
problem = Path.read_text(path)
positions = [int(i) for i in problem.strip().split(',')]

x_1 = min(positions)
x_2 = max(positions)

fuel = []
for x in range(x_1, x_2 + 1):
    f = 0
    for pos in positions:
        dist = max(x, pos) - min(x, pos)
        f += (dist * (dist + 1)) / 2
    fuel.append(f)

print(min(fuel))