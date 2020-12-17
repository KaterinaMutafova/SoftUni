targets = input().split()
targets = [int(el) for el in targets]

info_commands = input()

while not info_commands == "End":
    command, index, value = info_commands.split()
    index = int(index)
    value = int(value)

    if command == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.remove(targets[index])
        elif index > len(targets) - 1 or index < 0:
            pass


    elif command == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif command == "Strike":
        if index + value >= len(targets) or index - value < 0:
            print("Strike missed!")
        else:
            targets = targets[:(index - value)] + targets[(index + value + 1):]

    info_commands = input()

targets = list(map(lambda x: str(x), targets))

if info_commands == "End":
    print('|'.join(targets))


