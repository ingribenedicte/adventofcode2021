from pathlib import Path

path = Path('input\day1.txt')
problem = Path.read_text(path)
depths = problem.strip().split('\n')

# Part 1:
count = 0
for first, second in zip(depths[0:-1], depths[1:]):
    if int(second) > int(first):
        count += 1
print(count)

# Part 2:
measures = []
for i, depth in enumerate(depths):
    if i >= 3:
        measures.append(int(depth)+int(depths[i-1])+int(depths[i-2]))

count = 0
for first, second in zip(measures[0:-1], measures[1:]):
    if second > first:
        count += 1
print(count)