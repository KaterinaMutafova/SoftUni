#На първия ред – цената на леглото на котката - реално число в интервала [10.00... 300.00]
#На втория ред – цената на тоалетната за котката за един месец - реално число в интервала [10.00…200.00]

cat_bed = float(input())
cat_toilet_month = float(input())

#Храната на котката за месец е с 25% по-скъпа от тоалетната,
#а играчките са с 50 % по-евтини от храната.
#Посещението при ветеринар на месец е с 10% по-скъпо от играчките.
#Всеки месец трябва да се отделят средства за непредвидени разходи,
#които са 5% от общият разход за 1 месец.

cat_food = cat_toilet_month + 0.25 * cat_toilet_month
cat_toys = 0.50 * cat_food
cat_vet = cat_toys + 0.10 * cat_toys

cat_expense_month = cat_food + cat_toilet_month + cat_toys + cat_vet
cat_extra_expense = 0.05 * cat_expense_month
total_expense_month = cat_expense_month + cat_extra_expense

total_expense = cat_bed + total_expense_month * 12

print(f"{total_expense:.2f} lv.")


