class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


products = []
data = input()
while not data == "buy":
    name, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)
    if name in map(lambda x: x.name, products):
        product = list(filter(lambda x: x.name == name, products))[0]
        product.price = price
        product.quantity += quantity
    else:
        product = Product(name, price, quantity)
        products.append(product)

    data = input()

for product in products:
    total_price = product.price * product.quantity
    print(f"{product.name} -> {total_price:.2f}")