with open("input.txt", "r") as file:
    energies = []
    energy = 0
    for line in file:
        if (line == "\n"):
            energies.append(energy)
            energy = 0
        else:
            energy += int(line)

    energies.append(energy)
    energies = sorted(energies, reverse=True)
    answer = sum(energies[:3])
    print(answer)