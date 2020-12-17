command = input()
dict_product = {}

while not command == "statistics":
    product_stats = command.split(":")
    key = product_stats[0]
    value = int(product_stats[1])
    if key not in dict_product:
        dict_product[key] = value
    else:
        dict_product[key] += value

    command = input()

print("Products in stock:")
for (product,quantity) in dict_product.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(dict_product.keys())}")
print(f"Total Quantity: {sum(dict_product.values())}")

