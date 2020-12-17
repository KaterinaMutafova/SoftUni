energy = 100
coins = 100

events_list = input().split("|")

is_bankrupt = False

for event in events_list:
    event_ingredient, value = event.split("-")
    value = int(value)

    if is_bankrupt:
        break

    if event_ingredient == "rest":
        if energy + value <= 100:
            gained_energy_value = value
            energy += gained_energy_value

        else:
            gained_energy_value = 0

        print(f"You gained {gained_energy_value} energy.")
        print(f"Current energy: {energy}.")

    elif event_ingredient == "order":
        if energy < 30:
            gained_energy_value = 50
            energy += gained_energy_value
            print("You had to rest!")
            continue
        lost_energy_value = 30
        energy -= lost_energy_value
        gained_coins = value
        coins += gained_coins
        print(f"You earned {gained_coins} coins.")
    else:
        if coins <= value:
            print(f"Closed! Cannot afford {event_ingredient}.")
            is_bankrupt = True
            break

        spent_coins = value
        coins -= spent_coins
        print(f"You bought {event_ingredient}.")


if not is_bankrupt:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")


#order-10|order-10|order-10|flour-100|order-100|oven-100|order-1000



