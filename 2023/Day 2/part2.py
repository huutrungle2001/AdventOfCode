def get_cubes(sets):
    sets = sets.split(", ")
    color_map = {"red": 0, "green": 0, "blue": 0}
    for color in sets:
        color = color.split(" ")
        color_map[color[1]] += int(color[0])
    return (color_map["red"], color_map["green"], color_map["blue"])


def get_max_cube(cubes):
    return (max(cube[0] for cube in cubes),
            max(cube[1] for cube in cubes),
            max(cube[2] for cube in cubes))


with open("input.txt", "r") as file:
    count = 0
    for line in file:
        sets = line.strip().split(": ")[1].split("; ")
        cubes = [get_cubes(line) for line in sets]
        red, green, blue = get_max_cube(cubes)
        count += red * green * blue
    print(count)
