def is_overlapped(segments):
    segments.sort(key=lambda x: x[0])
    first, second = segments
    return (
        (first[0] <= second[0]
         and first[1] >= second[0])
        or
        (first[0] >= second[0]
            and first[0] <= second[1])
    )


with open("input.txt", "r") as file:
    count = 0
    for line in file:
        segments = [[int(x) for x in segment.split("-")]
                    for segment in line.split(",")]
        if is_overlapped(segments):
            count += 1
    print(count)
