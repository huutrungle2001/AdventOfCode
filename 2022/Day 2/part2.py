# Opponent:
#   A: Rock
#   B: Paper
#   C: Scissors
# You:
#   X: Lose
#   Y: Draw
#   Z: Win
# Score:
#   Rock: 1
#   Paper: 2
#   Scissors: 3
#   Lose: 0
#   Draw: 3
#   Win: 6

guide_map = {"A": {"X": 3, "Y": 4, "Z": 8},
             "B": {"X": 1, "Y": 5, "Z": 9},
             "C": {"X": 2, "Y": 6, "Z": 7}}

with open("input.txt", "r") as file:
    total_score = 0
    for line in file:
        opponent = line[0]
        you = line[2]
        total_score += guide_map[opponent][you]
    print(total_score)
