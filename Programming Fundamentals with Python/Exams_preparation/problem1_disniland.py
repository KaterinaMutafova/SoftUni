budget = float(input())
months_left = int(input())

saved_money = 0
currently_saved_money = 0
money_for_clothes = 0
bonus = 0

for month in range(1, months_left + 1):
    if month != 1 and not month % 2 == 0:
        money_for_clothes = 0.16 * saved_money
        saved_money -= money_for_clothes
    if month % 4 == 0:
        bonus = 0.25 * saved_money
        saved_money += bonus

    currently_saved_money = 0.25 * budget
    saved_money += currently_saved_money


if saved_money >= budget:
    money_for_souvenirs = saved_money - budget
    print(f"Bravo! You can go to Disneyland and you will have {money_for_souvenirs:.2f}lv. for souvenirs.")
elif saved_money < budget:
    missing_money = budget - saved_money
    print(f"Sorry. You need {missing_money:.2f}lv. more.")
