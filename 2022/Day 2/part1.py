# Opponent:
#   A: Rock
#   B: Paper
#   C: Scissors
# You:
#   X: Rock
#   Y: Paper
#   Z: Scissors
# Score:
#   Rock: 1
#   Paper: 2
#   Scissors: 3
#   Tie: 3
#   Win: 6
#   Lose: 0

shape_map = {"A": "X", "B": "Y", "C": "Z"}
score_map = {"X": 1, "Y": 2, "Z": 3}


def get_score(opponent, you):
    if opponent == you:
        return 3
    elif opponent == "X":
        if you == "Y":
            return 6
        else:
            return 0
    elif opponent == "Y":
        if you == "Z":
            return 6
        else:
            return 0
    elif opponent == "Z":
        if you == "X":
            return 6
        else:
            return 0


with open("input.txt", "r") as file:
    total_score = 0
    for line in file:
        opponent = line[0]
        you = line[2]
        total_score += get_score(shape_map[opponent], you) + score_map[you]
    print(total_score)
