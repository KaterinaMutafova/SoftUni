items_list = input().split("|")
budget = float(input())

new_prices = []

price_clothes = 50.00
price_shoes = 35.00
price_accessories = 20.50
overall_profit = 0

for item_data in items_list:
    item_type, item_value = item_data.split("->")
    item_value = float(item_value)

    if item_type == "Clothes" and item_value > 50:
        continue
    elif item_type == "Shoes" and item_value > 35:
        continue
    elif item_type == "Accessories" and item_value > 20.50:
        continue

    if budget > item_value:
        budget -= item_value
        current_profit = 0.4 * item_value
        overall_profit += current_profit
        new_prices.append(item_value + current_profit)


for single_price in new_prices:
    print(f"{single_price:.2f}", end=" ")

print()
print(f"Profit: {overall_profit:.2f}")

budget += sum(new_prices)

if budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")


# Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60