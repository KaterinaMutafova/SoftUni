num_of_trains = int(input())

trains_list = [0 for _ in range(num_of_trains)]

command = input()

while not command == "End":
    data = command.split()
    if data[0] == "add":
        number_of_people = int(data[1])
        trains_list[-1] += number_of_people
    elif data[0] == "insert":
        index = int(data[1])
        number_of_people = int(data[2])
        trains_list[index] += number_of_people
    elif data[0] == "leave":
        index = int(data[1])
        number_of_people = int(data[2])
        trains_list[index] -= number_of_people

    command = input()

print(trains_list)