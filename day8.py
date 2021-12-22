from pathlib import Path

path = Path('input\day8.txt')
problem = Path.read_text(path)
segments = problem.strip().split('\n')

values = []

for segment in segments:
    segment = segment.split(' ')
    segment.remove('|')

    one = set()
    two = set()
    four = set()
    seven = set()
    eight = set()
    nine = set()

    for s in segment:
        if len(s) == 2:
            one = set(s)
        if len(s) == 3:
            seven = set(s)
        if len(s) == 4:
            four = set(s)
        if len(s) == 7:
            eight = set(s)
        if len(seven) == 3 and len(one) == 2:
            top = seven - one
        if len(seven) == 3 and len(four) == 4:
            top = seven - seven.intersection(four)

    for s in segment:
        if len(s) == 6:
            unknown_set = set(s)
            if len(four.union(seven)) == 5 and four.union(seven).issubset(unknown_set):
                nine = unknown_set
                bottom = nine - four - seven
                lower_left = eight - nine

    for s in segment:
        if len(s) == 5:
            unknown_set = set(s)
            if top.union(bottom, lower_left).issubset(unknown_set):
                two = unknown_set
                middle = two.intersection(four - one)
                upper_left = four - one - middle
                upper_right = two - middle - bottom - top - lower_left

    lower_right = eight - top - bottom - middle - lower_left - upper_left - upper_right

    zero = seven.union(upper_left, lower_left, bottom)
    three = seven.union(middle, bottom)
    five = top.union(upper_left, middle, lower_right, bottom)
    six = five.union(lower_left)

    configuration = [zero, one, two, three, four, five, six, seven, eight, nine]
    conf_digits = [i for i in range (10)]

    value = 0
    for i, s in enumerate(segment[-5:]):
        z = set(s)
        for j, c in enumerate(configuration):
            if z == c:
                value += conf_digits[j] * 10**(4 - i)

    if value > 9999:
        value = value % 10000
    values.append(value)

print(sum(values))
