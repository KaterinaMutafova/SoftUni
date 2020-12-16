#Ред 1. Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
#Ред 2. Брой на статистите – цяло число в интервала [1 … 500]
#Ред 3. Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]

movie_budget = float(input())   #movie_budget > 1.00    #movie_budget < 1000000.00ice
count_stat = int(input())
price_clothes_per_one_stat = float(input())

#logic
decor = movie_budget * 0.10
price_all_clothes = count_stat * price_clothes_per_one_stat

if count_stat > 150:
    price_all_clothes = price_all_clothes * 0.90

price_dec_and_cloth = decor + price_all_clothes

left_money = movie_budget - price_dec_and_cloth
if price_dec_and_cloth > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(left_money):.2f} leva more.")
elif price_dec_and_cloth <= movie_budget:
    print("Action!")
    print(f"Wingard starts filming with {abs(left_money):.2f} leva left.")

