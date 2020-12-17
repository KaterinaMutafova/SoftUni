targets = input().split()
targets = [int(el) for el in targets]

count_shot_target = 0
command = input()

while not command == "End":
    index = int(command)
    if index < len(targets) and targets[index] != -1:
        shot_target = targets[index]
        targets[index] = -1
        count_shot_target += 1
        for i in range(len(targets)):
            if targets[i] > shot_target and targets[i] != -1:
                targets[i] -= shot_target
            elif targets[i] <= shot_target and targets[i] != -1:
                targets[i] += shot_target

    command = input()

print(f"Shot targets: {count_shot_target} -> {' '.join(str(num) for num in targets)}")
