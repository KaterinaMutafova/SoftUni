# Shadowmourne – requires 250 Shards;
# Valanyr – requires 250 Fragments;
# Dragonwrath – requires 250 Motes;


mapper_legend = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
dict_key_materials = {"shards": 0, "fragments": 0, "motes": 0}

legendary_item = ""

dict_junk_materials = {}

shards = 0
fragments = 0
motes = 0

materials = input()
while True:
    list_materials = materials.split(" ")
    is_found_legend = False
    for i in range(0, len(list_materials), 2):
        material = list_materials[i + 1].lower()
        quantity = int(list_materials[i])
        if material in dict_key_materials:
            dict_key_materials[material] += quantity
        else:
            if material not in dict_junk_materials:
                dict_junk_materials[material] = quantity
            else:
                dict_junk_materials[material] += quantity
        for key, value in dict_key_materials.items():
            if value >= 250:
                print(f"{mapper_legend[key]} obtained!")
                dict_key_materials[key] -= 250
                is_found_legend = True

        if is_found_legend:
            break
    if is_found_legend:
        break

    materials = input()

ordered_key_materials = sorted(dict_key_materials.items(), key=lambda x: (-x[1], x[0]))
sorted_junk_materials = sorted(dict_junk_materials.items(),key=lambda x: x[0])

for item, quantity in ordered_key_materials:
    print(f"{item}: {quantity}")

for junk_item, junk_quantity in sorted_junk_materials:
    print(f"{junk_item}: {junk_quantity}")





