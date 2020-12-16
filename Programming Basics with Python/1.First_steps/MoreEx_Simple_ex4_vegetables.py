#Първи ред – Цена за килограм зеленчуци – реално число[0.00… 1000.00]
#Втори ред – Цена за килограм плодове – реално число[0.00… 1000.00]
#Трети ред – Общо килограми на зеленчуците – цяло число[0… 1000]
#Четвърти ред – Общо килограми на плодовете – цяло число[0… 1000]

veg_lv_per_kg = float(input())
fruit_lv_per_kg = float(input())
veg_amount_kg_total = float(input())
fruit_amount_kg_total = float(input())

#logic
price_veg_lv = veg_lv_per_kg * veg_amount_kg_total
price_fruit_lv = fruit_lv_per_kg * fruit_amount_kg_total

price_all_lv = price_veg_lv + price_fruit_lv
price_all_eu = price_all_lv / 1.94

print(f"{price_all_eu:.2f}")

