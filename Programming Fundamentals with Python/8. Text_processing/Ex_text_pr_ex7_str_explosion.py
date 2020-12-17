# Exploding a number of digits and letters after the symbol ">" with the given power

line = input()
index = 0
strength = 0
new_list_line = []

for index in range(len(line)):
    if line[index] == ">":
        new_list_line.append(line[index])
        strength += int(line[index + 1])

    elif not line[index] == ">" and strength > 0:
        strength -= 1

    elif not line[index] == ">" and strength == 0:
        new_list_line.append(line[index])


print(''.join(new_list_line))






