#От конзолата се четат 5 реда:
#1. Броят на дните, в които тече кампанията – цяло число;
#2. Броят на сладкарите – цяло число;
#3. Броят на тортите – цяло число;
#4. Броят на гофретите – цяло число;
#5. Броят на палачинките – цяло число.

#Торта - 45 лв.
#Гофрета - 5.80 лв.
#Палачинка – 3.20 лв.

days_campain = int(input())
number_bakers = int(input())
number_cakes = int(input())
number_gofrettes = int(input())
number_pancakes = int(input())

#logic

sum_cakes_per_day = number_cakes * 45 * number_bakers
sum_gofrettes_per_day = number_gofrettes * 5.80 * number_bakers
sum_pancakes_per_day = number_pancakes * 3.20 * number_bakers
all_per_day = sum_cakes_per_day + sum_gofrettes_per_day + sum_pancakes_per_day

expence = (1/8) * all_per_day * days_campain
charity_sum = all_per_day * days_campain - expence

print(charity_sum)


