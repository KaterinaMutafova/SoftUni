count_commands = int(input())

database_parking = {}

for count_user in range(count_commands):
    command = input().split()
    car_user = command[1]
    if command[0] == "register":
        car_number = command[2]
        if car_user not in database_parking:
            database_parking[car_user] = car_number
            print(f"{car_user} registered {car_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {database_parking[car_user]}")
    elif command[0] == "unregister":
        if car_user not in database_parking:
            print(f"ERROR: user {car_user} not found")
        else:
            print(f"{car_user} unregistered successfully")
            database_parking.pop(car_user)

for car_user, car_number in database_parking.items():
    print(f"{car_user} => {car_number}")
