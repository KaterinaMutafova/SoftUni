#Вид цветя - текст с възможности Roses, Dahlias, Tulips, Narcissus или Gladiolus;
#Брой цветя - цяло число;
#Бюджет - цяло число.

flower_type = input()
flower_count = int(input())
budget = float(input())

price_lv = 0

if flower_type == "Roses":
    price_lv = 5
    if flower_count > 80:
        price_lv = 0.9 * price_lv

if flower_type == "Dahlias":
    price_lv = 3.8
    if flower_count > 90:
        price_lv = 0.85 * price_lv

if flower_type == "Tulips":
    price_lv = 2.8
    if flower_count > 80:
        price_lv = 0.85 * price_lv

if flower_type == "Narcissus":
    price_lv = 3
    if flower_count < 120:
        price_lv = 1.15 * price_lv

if flower_type == "Gladiolus":
    price_lv = 2.5
    if flower_count < 80:
        price_lv = 1.2 * price_lv

end_price = price_lv * flower_count
diff = budget - end_price

if end_price > budget:
    print(f"Not enough money, you need {abs(diff):.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {diff:.2f} leva left.")




