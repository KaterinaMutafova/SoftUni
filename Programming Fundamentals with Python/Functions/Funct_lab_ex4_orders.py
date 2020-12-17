product = input()
product_quantity = int(input())


def orders(type_of_item, count_of_item):
    coffee_price = 1.50
    water_price = 1.00
    coke_price = 1.40
    snacks_price = 2.00
    if type_of_item == "coffee":
        total_price = coffee_price * count_of_item
    elif type_of_item == "water":
        total_price = water_price * count_of_item
    elif type_of_item == "coke":
        total_price = coke_price * count_of_item
    elif type_of_item == "snacks":
        total_price = snacks_price * count_of_item
    return total_price


print(f"{orders(product, product_quantity):.2f}")
