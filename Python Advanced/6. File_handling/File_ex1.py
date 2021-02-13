import re


def replace_symbols(line):
    return re.sub(r"[,.!?-]", "@", line)


with open("text.txt", "r") as file:
    lines = file.readlines()
    for row in range(len(lines)):
        if row % 2 == 0:
            replaced = replace_symbols(lines[row]).split()
            print(' '.join(replaced[::-1]))














