from pathlib import Path

path = Path('navigation.txt')
problem = Path.read_text(path)
nav_lines = problem.strip().split('\n')

chars = {'[': ']', '{': '}', '(': ')', '<': '>'}

# Part 1:
corrupted_chars = []
corrupted_lines = []
for n, nav_line in enumerate(nav_lines):
    chunks = []
    for i, char in enumerate(nav_line):
        if char in set(chars.keys()):
            chunks.append(char)
        if char in set(chars.values()):
            opening_char = chunks.pop()
            closing_char = char
            if closing_char != chars[opening_char]:
                corrupted_chars.append(closing_char)
                corrupted_lines.append(n)
                break

#print(corrupted_chars)

syntax_error_score = 0
for char in corrupted_chars:
    if char == ')':
        syntax_error_score += 3
    if char == ']':
        syntax_error_score += 57
    if char == '}':
        syntax_error_score += 1197
    if char == '>':
        syntax_error_score += 25137

# Part 2:
incomplete_lines = []
for i, nav_line in enumerate(nav_lines):
    if len(corrupted_lines) > 0 and i == corrupted_lines[0]:
        corrupted_lines.pop(0)
    else:
        incomplete_lines.append(nav_line)

completion = []
for nav_line in incomplete_lines:
    chunks = []
    missing_chars = []
    for i, char in enumerate(nav_line):
        if char in set(chars.keys()):
            chunks.append(char)
        if char in set(chars.values()):
            chunks.pop()
    for c in reversed(chunks):
        missing_chars.append(chars[c])
    completion.append(missing_chars)

print(completion)

total_scores = []
for c in completion:
    total_score = 0
    for s in c:
        total_score *= 5
        if s == ')':
            total_score += 1
        if s == ']':
            total_score += 2
        if s == '}':
            total_score += 3
        if s == '>':
            total_score += 4
    total_scores.append(total_score)


sorted_scores = sorted(total_scores)
middle_index = int(((len(sorted_scores) + 1) / 2) - 1)
print(sorted_scores)
print(sorted_scores[middle_index])