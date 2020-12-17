shopping_list = input().split("!")

command = input()


def check_item_exists(items_list, searched_item):
    return True if searched_item in items_list else False


while not command == "Go Shopping!":
    command_type = command.split()[0]
    item = command.split()[1]

    if command_type == "Urgent":
        if not check_item_exists(shopping_list, item):
            shopping_list.insert(0, item)

    elif command_type == "Unnecessary":
        if check_item_exists(shopping_list, item):
            shopping_list.remove(item)

    elif command_type == "Correct":
        if check_item_exists(shopping_list, item):
            new_item = command.split()[2]
            index_to_switch = shopping_list.index(item)
            shopping_list.remove(item)
            shopping_list.insert(index_to_switch, new_item)

    elif command_type == "Rearrange":
        if check_item_exists(shopping_list, item):
            shopping_list.remove(item)
            shopping_list.append(item)

    command = input()

string_list = ", ".join(shopping_list)
print(string_list)
