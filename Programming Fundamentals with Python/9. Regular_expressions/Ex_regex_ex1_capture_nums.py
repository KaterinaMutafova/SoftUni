import re

pattern = r"\d+"

list_num = []

data = input()

while data:
    match = re.findall(pattern, data)
    if match:
        list_num.extend(match)

    data = input()


print(' '.join(list_num))

