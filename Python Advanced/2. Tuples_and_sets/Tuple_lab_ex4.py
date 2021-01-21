cars_count = int(input())

parking_lot = set()

for car in range(cars_count):
    direction, number = input().split(", ")
    if direction == "IN":
        parking_lot.add(number)
    elif direction == "OUT":
        parking_lot.remove(number)


if parking_lot:
    for car_number in parking_lot:
        print(car_number)
else:
    print("Parking Lot is Empty")



