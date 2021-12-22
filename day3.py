from pathlib import Path
from collections import Counter

path = Path('input\day3.txt')
problem = Path.read_text(path)
diagnostics = problem.strip().split('\n')

# Part 1:
count_ones = [0]*12
count_zeros = [0]*12
for diagnostic in diagnostics:
    for i, char in enumerate(diagnostic):
        if int(char) == 0:
            count_zeros[i] += 1
        if int(char) == 1:
            count_ones[i] += 1

gamma_str = ''
epsilon_str = ''
for i, j in zip(count_ones, count_zeros):
    if i > j:
        gamma_str = gamma_str + '1'
        epsilon_str = epsilon_str + '0'
    else:
        gamma_str = gamma_str + '0'
        epsilon_str = epsilon_str + '1'

gamma = int(gamma_str, base = 2)
epsilon = int(epsilon_str, base = 2)
print(gamma * epsilon)

# Part 2:
for i in range(12):
    count_zeros = 0
    count_ones = 0
    for diagnostic in diagnostics:
        if diagnostic[i] == '0':
            count_zeros += 1
        if diagnostic[i] == '1':
            count_ones += 1
    if count_ones >= count_zeros:
        diagnostics = [x for x in diagnostics if x[i] == '1']
    else:
        diagnostics = [x for x in diagnostics if x[i] == '0']

oxygen_generator_rating = int(diagnostics[0], base = 2)

diagnostics = problem.split('\n')
for i in range(12):
    count_zeros = 0
    count_ones = 0
    for diagnostic in diagnostics:
        if diagnostic[i] == '0':
            count_zeros += 1
        if diagnostic[i] == '1':
            count_ones += 1
    if count_ones >= count_zeros:
        diagnostics = [x for x in diagnostics if x[i] == '0']
    else:
        diagnostics = [x for x in diagnostics if x[i] == '1']
    if len(diagnostics) == 1:
        break

co2_scrubber_rating = int(diagnostics[0], base = 2)
print(oxygen_generator_rating * co2_scrubber_rating)