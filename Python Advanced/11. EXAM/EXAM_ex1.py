from collections import deque

dict_fireworks = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}
firework_show_done = False

firework_effects = deque([int(el) for el in input().split(", ")])
explosive_power = [int(el) for el in input().split(", ")]

while True:
    if dict_fireworks["Palm Fireworks"] >= 3 \
        and dict_fireworks["Willow Fireworks"] >= 3 \
        and dict_fireworks["Crossette Fireworks"] >= 3:
        firework_show_done = True
        break
    if len(firework_effects) == 0 or len(explosive_power) == 0:
        break

    if firework_effects[0] <= 0:
        firework_effects.popleft()
        continue
    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue

    current_sum = firework_effects[0] + explosive_power[-1]

    if current_sum % 3 == 0 and current_sum % 5 != 0:
        dict_fireworks["Palm Fireworks"] += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif current_sum % 5 == 0 and current_sum % 3 != 0:
        dict_fireworks["Willow Fireworks"] += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif current_sum % 5 == 0 and current_sum % 3 == 0:
        dict_fireworks["Crossette Fireworks"] += 1
        firework_effects.popleft()
        explosive_power.pop()
    else:
        firework_effects[0] -= 1
        firework_effects.append(firework_effects.popleft())
        continue

if firework_show_done:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")

if len(firework_effects) > 0:
    print(f"Firework Effects left: {', '.join(str(el) for el in firework_effects)}")
if len(explosive_power) > 0:
    print(f"Explosive Power left: {', '.join(str(el) for el in explosive_power)}")

for firework, quantity in dict_fireworks.items():
    print(f"{firework}: {quantity}")
