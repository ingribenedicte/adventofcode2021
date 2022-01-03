from pathlib import Path
import numpy as np

path = Path('input\day13.txt')
problem = Path.read_text(path)
dots, instructions = problem.strip().split('\n\n')

dots = dots.split('\n')
x_list = []
y_list = []
for dot in dots:
    x, y = dot.split(',')
    x_list.append(int(x))
    y_list.append(int(y))

mx = np.array([[0 for x in range(max(x_list) + 1)] for y in range(max(y_list) + 1)])

for x, y in zip(x_list, y_list):
    mx[y][x] = 1

mx_copy = np.copy(mx)
instructions = instructions.split('\n')

def fold(mx, axis, number):
    if axis == 'y':
        orig_mx = mx[0:number]
        fold_mx = mx[number + 1:]
        flip_mx = np.flipud(fold_mx)
    if axis == 'x':
        orig_mx = [row[0:number] for row in mx]
        fold_mx = [row[number + 1:] for row in mx]
        flip_mx = np.fliplr(fold_mx)
    return orig_mx + flip_mx


# Part 1:
axis, number = instructions[0].replace('fold along ', '').split('=')
mx = fold(mx, axis, int(number))
print(np.count_nonzero(mx))

# Part 2:
for instruction in instructions:
    axis, number = instruction.replace('fold along ', '').split('=')
    mx_copy = fold(mx_copy, axis, int(number))

mx_copy = np.where(mx_copy > 0, '#', mx_copy)
mx_copy = np.where(mx_copy == '0', '.', mx_copy)

print(mx_copy)