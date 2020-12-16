#Възрастта на Лили - цяло число в интервала [1...77]
#Цената на пералнята - число в интервала [1.00...10 000.00]
#Единична цена на играчка - цяло число в интервала [0...40]

age = int(input())
wash_mash_lv = float(input())
toy_lv = int(input())

cur_money_rd = 0
money_rd = 0
toys_count = 0
toys_sum = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money_rd += 10
        cur_money_rd = cur_money_rd + money_rd
        cur_money_rd -= 1
    else:
        toys_count += 1

toys_sum = toys_count * toy_lv

all_sum = cur_money_rd + toys_sum
left = 0
no_left = 0

if all_sum >= wash_mash_lv:
    left = all_sum - wash_mash_lv
    print(f"Yes! {left:.2f}")
else:
    no_left = wash_mash_lv - all_sum
    print(f"No! {no_left:.2f}")







