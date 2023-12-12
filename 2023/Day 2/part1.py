NUMS_RED = 12
NUMS_GREEN = 13
NUMS_BLUE = 14


def is_valid_set(cubes):
    return (cubes[0] <= NUMS_RED and
            cubes[1] <= NUMS_GREEN and
            cubes[2] <= NUMS_BLUE)


def get_cubes(line):
    line = line.split(", ")
    color_map = {"red": 0, "green": 0, "blue": 0}
    for color in line:
        color = color.split(" ")
        color_map[color[1]] += int(color[0])
    return (color_map["red"], color_map["green"], color_map["blue"])


with open("input.txt", "r") as file:
    count = 0
    game = 1
    for line in file:
        sets = line.strip().split(": ")[1].split("; ")
        cubes = [get_cubes(line) for line in sets]
        for cube in cubes:
            if not is_valid_set(cube):
                break
        else:
            count += game
        game += 1
    print(count)