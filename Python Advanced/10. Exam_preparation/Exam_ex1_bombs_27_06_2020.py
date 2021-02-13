from collections import deque

# DATURA_BOMBS = 40
# CHERRY_BOMBS = 60
# SMOKE_DECOY_BOMBS = 120

bomb_effects = deque([int(el) for el in input().split(", ")])
bomb_casings = [int(el) for el in input().split(", ")]

dict_bombs = {"Datura Bombs": 40, "Cherry Bombs": 60, "Smoke Decoy Bombs": 120}
bombs_pouch = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}
full_bomb_pouch = False

while True:
    if bombs_pouch["Datura Bombs"] >= 3 and bombs_pouch["Cherry Bombs"] >= 3 and bombs_pouch["Smoke Decoy Bombs"] >= 3:
        full_bomb_pouch = True
        break
    if len(bomb_effects) == 0:
        break
    if len(bomb_casings) == 0:
        break

    current_sum = bomb_effects[0] + bomb_casings[-1]

    if current_sum in dict_bombs.values():
        for key, value in dict_bombs.items():
            if value == current_sum:
                current_created_bomb = key
                bombs_pouch[key] += 1
                bomb_effects.popleft()
                bomb_casings.pop()
                break
    else:
        bomb_casings[-1] -= 5



if full_bomb_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if len(bomb_effects) == 0:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(str(el) for el in bomb_effects)}")

if len(bomb_casings) == 0:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(str(el) for el in bomb_casings)}")


bombs_pouch = sorted(bombs_pouch.items(), key=lambda x: x[0], reverse=False)
for bomb, quantity in bombs_pouch:
    print(f"{bomb}: {quantity}")









