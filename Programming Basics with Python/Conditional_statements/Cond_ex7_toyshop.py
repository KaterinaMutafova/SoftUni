
#1. Цена на екскурзията - реално число;
#2. Брой пъзели - цяло число;
#3. Брой говорещи кукли - цяло число;
#4. Брой плюшени мечета - цяло число;
#5. Брой миньони - цяло число;
#6. Брой камиончета - цяло число.


trip_price = float(input())
count_puzzles = int(input())
count_dolls = int(input())
count_bears = int(input())
count_minions = int(input())
count_trucks = int(input())

#Пъзел - 2.60 лв.
#Говореща кукла - 3 лв.
#Плюшено мече - 4.10 лв.
#Миньон - 8.20 лв.
#Камионче - 2 лв.

price_puzzles = count_puzzles * 2.60
price_dolls = count_dolls * 3
price_bears = count_bears * 4.10
price_minions = count_minions * 8.20
price_trucks = count_trucks * 2

total_price = price_puzzles + price_dolls + price_bears + price_minions + price_trucks

count_toys = count_puzzles + count_dolls + count_bears + count_minions + count_trucks
discount = 0
total_price_reduce = total_price - discount

if count_toys >= 50:
    discount = 0.25 * total_price
    total_price_reduce = total_price - discount

total_price_reduce_2 = total_price_reduce - total_price_reduce * 0.10

gain_price = abs(total_price_reduce_2 - trip_price)

if total_price_reduce_2 >= trip_price:
    print(f"Yes! {gain_price:.2f} lv left.")
else:
    print(f"Not enough money! {gain_price:.2f} lv needed.")







