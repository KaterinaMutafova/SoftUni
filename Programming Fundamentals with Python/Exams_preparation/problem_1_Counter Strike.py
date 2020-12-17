energy = int(input())
won_battles = 0

distance_command = input()

while not distance_command == "End of battle":
    distance_command = int(distance_command)
    if distance_command > energy:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        break
    else:
        energy -= distance_command
        won_battles += 1
        if won_battles % 3 == 0:
            energy += won_battles

    distance_command = input()

if distance_command == "End of battle":
    print(f"Won battles: {won_battles}. Energy left: {energy}")




