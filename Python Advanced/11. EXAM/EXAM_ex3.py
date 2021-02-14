def stock_availability(*args):
    inventory_list = args[0]
    action = args[1]

    if action == "delivery":
        delivery_boxes = list(args[2:])
        inventory_list.extend(delivery_boxes)
    elif action == "sell":
        if len(args) == 2:
            inventory_list.remove(inventory_list[0])

        else:
            if type(args[2]) == int:
                number_of_boxes = args[2]
                for _ in range(number_of_boxes):
                    inventory_list.remove(inventory_list[0])
            elif type(args[2]) == str:
                products_to_sell = args[2:]
                for product in products_to_sell:
                    if product in inventory_list:
                        while product in inventory_list:
                            inventory_list.remove(product)


    return inventory_list




print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
