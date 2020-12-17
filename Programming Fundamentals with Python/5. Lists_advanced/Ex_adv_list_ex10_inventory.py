inventory = input().split(", ")


while True:
    info = input()
    if info == "Craft!":
        break

    command, item = info.split(" - ")
    if command == "Collect":
        if item not in inventory:
            inventory.append(item)
        else:
            pass

    elif command == "Drop":
        if item in inventory:
            inventory.remove(item)
        else:
            pass

    elif command == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in inventory:
            for index in range(len(inventory)):
                if inventory[index] == old_item:
                    inventory.insert(index+1, new_item)

    elif command == "Renew":
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)


inventory_string = ", ".join(inventory)
print(inventory_string)

