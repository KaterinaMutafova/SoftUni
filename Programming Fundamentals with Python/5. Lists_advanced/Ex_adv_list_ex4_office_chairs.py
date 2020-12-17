num_of_rooms = int(input())

list_of_rooms = [input() for n in range(num_of_rooms)]

free_chairs = []
needed_chairs = []
enough_chairs = True
iteration_room_number = 0

for i in list_of_rooms:
    room_chairs = i.split(" ")
    iteration_room_number += 1
    if len(room_chairs[0]) >= int(room_chairs[1]):
        extra_chairs = len(room_chairs[0]) - int(room_chairs[1])
        free_chairs.append(extra_chairs)
    elif len(room_chairs[0]) < int(room_chairs[1]):
        less_chairs = int(room_chairs[1]) - len(room_chairs[0])
        needed_chairs.append(less_chairs)
        print(f"{less_chairs} more chairs needed in room {iteration_room_number}")
        enough_chairs = False

if enough_chairs:
    print(f"Game On, {sum(free_chairs)} free chairs left")













