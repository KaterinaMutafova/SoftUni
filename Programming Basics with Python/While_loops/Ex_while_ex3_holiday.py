#Пари, нужни за екскурзията - реално число;
#Налични пари - реално число.
#След това многократно се четат по два реда:
#Вид действие – текст с две възможности: spend или save;
#Сумата, която ще спести/похарчи - реално число.

money_trip = float(input())
saved_money = float(input())
count = 0
count_spend = 0
money_is_saved = False

while True:
    action = input()
    money = float(input())
    count += 1

    if action == "save":
        saved_money += money
        count_spend = 0
    elif action == "spend":
        count_spend += 1
        if money > saved_money:
            money = saved_money
            saved_money = 0
        elif money < saved_money:
            saved_money -= money
        if count_spend == 5:
            money_is_saved = False
            break

    if saved_money >= money_trip:
        money_is_saved = True
        break
    else:
        continue


if money_is_saved:
    print(f"You saved the money for {count} days.")
else:
    print(f"You can't save the money.")
    print(count)








