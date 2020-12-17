client_type = input()
price = 0
total_price = 0
taxes = 0

while not (client_type == "special" or client_type == "regular"):
    current_price = float(client_type)
    if current_price <= 0:
        print("Invalid price!")
    else:
        price += current_price

    client_type = input()



if client_type == "regular":
    taxes = price * 0.20
    total_price = price + taxes

elif client_type == "special":
    taxes = price * 0.20
    total_price = price + taxes
    discount = 0.10 * total_price
    total_price -= discount

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")






