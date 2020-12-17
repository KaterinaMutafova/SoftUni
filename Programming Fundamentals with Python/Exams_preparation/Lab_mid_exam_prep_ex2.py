count_of_people = int(input())
wagons = [int(el) for el in input().split()]
MAX_SEATS_WAGON = 4


for index in range(len(wagons)):
    taken_seats = wagons[index]
    available_seats = MAX_SEATS_WAGON - taken_seats
    if count_of_people >= available_seats:
        count_of_people -= available_seats
        wagons[index] += available_seats
    elif count_of_people < available_seats:
        wagons[index] += count_of_people
        available_seats = MAX_SEATS_WAGON - count_of_people
        count_of_people -= count_of_people

if sum(wagons) < len(wagons) * MAX_SEATS_WAGON:
    print("The lift has empty spots!")
elif count_of_people > 0:
    print(f"There isn't enough space! {count_of_people} people in a queue!")

print(" ".join(str(el) for el in wagons))







