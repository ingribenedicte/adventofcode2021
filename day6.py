from pathlib import Path

path = Path('input\day6.txt')
problem = Path.read_text(path)
lanternfish = [int(i) for i in problem.split(',')]

timers = [0 for _ in range(9)]
for lf in lanternfish:
    timers[lf] += 1

for day in range(1, 256 + 1):
    newborns = timers[0]
    for i in range(8):
        timers[i] = timers[i + 1]
    timers[6] += newborns
    timers[8] = newborns

print(sum(timers))