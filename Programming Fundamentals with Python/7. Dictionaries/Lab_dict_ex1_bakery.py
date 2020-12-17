line_food_quantity = input().split(" ")

dict_food = {}

for item in range(0, len(line_food_quantity), 2):
    key = line_food_quantity[item]
    value = line_food_quantity[item + 1]
    dict_food[key] = int(value)

print(dict_food)