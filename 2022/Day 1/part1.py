with open("input.txt", "r") as file:
    max_sum = -float("inf")
    temp_sum = 0
    for line in file:
        if (line == "\n"):
            max_sum = max(max_sum, temp_sum)
            temp_sum = 0
        else:
            temp_sum += int(line)
    max_sum = max(max_sum, temp_sum)
    print(max_sum)
