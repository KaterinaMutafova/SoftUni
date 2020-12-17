# Ornament Set – 2$ a piece
# Tree Skirt – 5$ a piece
# Tree Garlands – 3$ a piece
# Tree Lights – 15$ a piece

quantity = int(input())
days_left = int(input())

ornament_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15

total_price = 0
spirit = 0

for day in range(1,days_left + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_price += ornament_price * quantity
        spirit += 5
    if day % 3 ==0:
        total_price += (tree_skirt_price + tree_garlands_price) * quantity
        spirit += 13
    if day % 5 == 0:
        total_price += tree_lights_price * quantity
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        total_price += tree_skirt_price + tree_garlands_price + tree_lights_price


    if day == days_left and day % 10 == 0:
        spirit -= 30

print(f"Total cost: {total_price}")
print(f"Total spirit: {spirit}")





