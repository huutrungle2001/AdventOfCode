import re

numbers = {"one": "1", "two": "2", "three": "3", "four": "4",
           "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def get_position_from_line(line):
    positions = []
    for key, value in numbers.items():
        positions += [match.span() for match in re.finditer(key, line)]
        positions += [match.span() for match in re.finditer(value, line)]
    return positions


def get_number_from_position(line, position):
    try:
        return numbers[line[position[0]:position[1]]]
    except KeyError:
        return line[position[0]:position[1]]


with open("input.txt") as file:
    total = 0
    for line in file:
        positions = get_position_from_line(line)
        min_position = min(positions, key=lambda x: x[0])
        max_position = max(positions, key=lambda x: x[1])
        number = get_number_from_position(line, min_position) + \
            get_number_from_position(line, max_position)
        total += int(number)
    print(total)
