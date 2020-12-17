def include_shop(shop_list, shop_name):
    shop_list.append(shop_name)
    return shop_list


def visit_shop(shop_list, type_shops, count_to_visit):
    if count_to_visit <= len(shop_list):
        if type_shops == "first":
            for time in range(count_to_visit):
                shop_list.remove(shop_list[0])


        elif type_shops == "last":
            for time in range(count_to_visit):
                shop_list.remove(shop_list[-1])

    return shop_list


def prefer_shop(shop_list, index_1, index_2):
    if 0 <= index_1 < len(shop_list) and 0 <= index_2 < len(shop_list):
        shop_list[index_1], shop_list[index_2] = shop_list[index_2], shop_list[index_1]
    return shop_list


def place_shop(shop_list, new_shop, index):
    if index + 1 <= len(shop_list) - 1:
        shop_list.insert(index + 1, new_shop)
    return shop_list


shops = input().split()
count_visits = int(input())

for visit in range(count_visits):
    command = input().split()
    if command[0] == "Include":
        include_shop(shops, command[1])

    elif command[0] == "Visit":
        first_last_shop = command[1]
        number_value = int(command[2])
        visit_shop(shops, first_last_shop, number_value)

    elif command[0] == "Prefer":
        index_shop_1 = int(command[1])
        index_shop_2 = int(command[2])
        prefer_shop(shops, index_shop_1, index_shop_2)

    elif command[0] == "Place":
        shop_name = command[1]
        index_shop = int(command[2])
        place_shop(shops, shop_name, index_shop)

print("Shops left:")
print(' '.join(shops))




