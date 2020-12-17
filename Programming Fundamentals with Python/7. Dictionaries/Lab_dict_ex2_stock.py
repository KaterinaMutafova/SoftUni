food_list = input().split()
searched_items = input().split()

food_dict = {}

for item in range(0, len(food_list), 2):
    key = food_list[item]
    value = food_list[item + 1]
    food_dict[key] = int(value)

for searched_item in searched_items:
    if searched_item in food_dict:
        quantity = food_dict[searched_item]
        print(f"We have {quantity} of {searched_item} left")
    else:
        print(f"Sorry, we don't have {searched_item}")