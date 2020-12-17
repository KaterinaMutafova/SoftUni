n_lines = int(input())
tank_litres = 255
current_fill = 0

for i in range(0, n_lines):
    litres = int(input())
    if tank_litres - litres >= 0:
        tank_litres -= litres
        current_fill += litres
    else:
        print(f"Insufficient capacity!")

print(current_fill)
