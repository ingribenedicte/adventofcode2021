from pathlib import Path

path = Path('input\day2.txt')
problem = Path.read_text(path)
instructions = problem.strip().split('\n')

# Part 1:
x, y = 0, 0
for instruction in instructions:
    instruction = instruction.split(' ')
    if instruction[0] == 'down':
        y += int(instruction[1])
    if instruction[0] == 'up':
        y -= int(instruction[1])
    if instruction[0] == 'forward':
        x += int(instruction[1])
print(x*y)

# Part 2:
x, y, aim = 0, 0, 0
for instruction in instructions:
    instruction = instruction.split(' ')
    if instruction[0] == 'down':
        aim += int(instruction[1])
    if instruction[0] == 'up':
        aim -= int(instruction[1])
    if instruction[0] == 'forward':
        x += int(instruction[1])
        y += aim * int(instruction[1])
print(x*y)