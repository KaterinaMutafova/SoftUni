targets = [int(el) for el in input().split("|")]

points = 0

command = input()

while not command == "Game over":
    info = command.split()
    if info[0] == "Shoot":
        direction, index, length = info[1].split("@")
        index = int(index)
        length = int(length)
        if 0 <= index < len(targets):
            if direction == "Right":
                new_index = (index + length) % len(targets)

            elif direction == "Left":
                new_index = (index - length) % len(targets)

            if targets[new_index] >= 5:
                targets[new_index] -= 5
                points += 5
            elif targets[new_index] < 5:
                points += targets[new_index]
                targets[new_index] = 0
        else:
            pass

    elif info[0] == "Reverse":
        targets.reverse()

    command = input()

print(' - '.join(str(el) for el in targets))
print(f"Iskren finished the archery tournament with {points} points!")
