#1. Брой екскурзии до море – цяло число в интервала [1… 500]
#2. Брой екскурзии до планина – цяло число в интервала [1… 500]

#море("sea") на цена 680 лева и планина("mountain") на цена 499 лева.

trip_sea_count = int(input())
trip_mountain_count = int(input())

price = 0
sum_gain = 0
is_sold = False

line = input()

while line != "Stop":
    name_trip = line
    if name_trip == "sea":
        if trip_sea_count > 0:
            trip_sea_count -= 1
            price = 680
        elif trip_sea_count == 0:
            price = 0
    elif name_trip == "mountain":
        if trip_mountain_count > 0:
            trip_mountain_count -= 1
            price = 499
        elif trip_mountain_count == 0:
            price = 0
    sum_gain += price
    if  trip_sea_count == 0 and trip_mountain_count == 0:
        is_sold = True
        break

    line = input()

if is_sold:
    print(f" Good job! Everything is sold.")
    print(f"Profit: {sum_gain} leva.")
else:
    print(f"Profit: {sum_gain} leva.")


