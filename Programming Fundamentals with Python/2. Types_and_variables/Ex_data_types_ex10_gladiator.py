# lost_fights = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
#
# cost_equip = 0
# counter =0
#
# for lost_game in range (1, lost_fights + 1):
#     if lost_game % 2 == 0:
#         cost_equip += helmet_price
#     if lost_game % 3 == 0:
#         cost_equip += sword_price
#     if lost_game % 2 == 0 and lost_game % 3 == 0:
#         cost_equip += shield_price
#         counter += 1
#         if counter == 2:
#             cost_equip += armor_price
#
# print(f"Gladiator expenses: {cost_equip:.2f} aureus")


lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

cost_equip = 0
counter_helmet = 0
counter_sword = 0
counter_shield = 0
counter_armor = 0

for l_game in range (1, lost_fights + 1):
    if l_game % 2 == 0:
        counter_helmet += 1
    if l_game % 3 == 0:
        counter_sword += 1
    if l_game % 2 == 0 and l_game % 3 == 0:
        counter_shield += 1
        if counter_shield % 2 == 0 and counter_shield != 0:
            counter_armor += 1

cost_equip = helmet_price * counter_helmet + sword_price * counter_sword + shield_price * counter_shield + armor_price * counter_armor
print(f"Gladiator expenses: {cost_equip:.2f} aureus")



