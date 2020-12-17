health = 100
bitcoins = 0

room_number = 0

dungeon_rooms = input().split("|")

for room in dungeon_rooms:
    room_number += 1
    command, value = room.split()
    value = int(value)
    if command == "potion":
        if value + health <= 100:
            health += value
            print(f"You healed for {value} hp.")
            print(f"Current health: {health} hp.")
        else:
            value = 100 - health
            health += value
            print(f"You healed for {value} hp.")
            print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")

    else:
        health -= value
        if health > 0:
            print(f"You slayed {command}.")
        elif health <= 0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_number}")
            exit(0)

print(f"You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {health}")




