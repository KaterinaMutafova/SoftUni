command = input()

count_line = 0
dict_resources = {}
list_resources = []

while not command == "stop":
    list_resources.append(command)

    command = input()

count_line = 0
for item in range(len(list_resources)):
    count_line += 1
    if not count_line % 2 == 0:
        key = list_resources[item]
        value = int(list_resources[item + 1])
        if key not in dict_resources:
            dict_resources[key] = value
        else:
            dict_resources[key] += value

for (resource, quantity) in dict_resources.items():
    print(f"{resource} -> {quantity}")