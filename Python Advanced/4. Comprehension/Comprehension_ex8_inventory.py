heroes = input().split(", ")

dict_heroes = {}

for name in heroes:
    items, costs = [], []
    dict_heroes[name] = [items, costs]

line = input()

while not line == "End":
    data = line.split("-")
    name = data[0]
    item = data[1]
    cost = int(data[2])
    list1 = ["Items", item]
    list2 = ["Cost", cost]
    if not item in dict_heroes[name][0]:
        dict_heroes[name][0].append(item)
        dict_heroes[name][1].append(cost)

    line = input()


for name, data in dict_heroes.items():
    print(f"{name} -> Items: {len(data[0])}, Cost: {sum(data[1])}")

