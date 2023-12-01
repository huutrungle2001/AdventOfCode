def get_num_from_line(line):
    first_num = ""
    second_num = ""
    for char in line:
        if char.isdigit():
            first_num = char
            break
    for char in line[::-1]:
        if char.isdigit():
            second_num = char
            break
    return int(first_num + second_num)


with open("input.txt", "r") as file:
    total = 0
    for line in file:
        total += get_num_from_line(line)
    print(total)