#1. Цена на ягодите в лева – реално число;
#2. Количество на бананите в килограми – реално число;
#3. Количество на портокалите в килограми – реално число;
#4. Количество на малините в килограми – реално число;
#5. Количество на ягодите в килограми – реално число.

price_strawberry = float(input())
amount_bananas = float(input())
amount_oranges = float(input())
amount_raspberry = float(input())
amount_strawberry = float(input())

#logic
#цената на малините е на половина по-ниска от тази на ягодите;
#цената на портокалите е с 40% по-ниска от цената на малините;
#цената на бананите е с 80% по-ниска от цената на малините.

strawberry_sum = amount_strawberry * price_strawberry

price_raspberry = 0.5 * price_strawberry
price_oranges = price_raspberry - ((40/100) * price_raspberry)
price_bananas = price_raspberry - ((80/100) * price_raspberry)

raspberry_sum = amount_raspberry * price_raspberry
oranges_sum = amount_oranges * price_oranges
bananas_sum = amount_bananas * price_bananas

all_money = strawberry_sum + raspberry_sum + oranges_sum + bananas_sum
print(all_money)
