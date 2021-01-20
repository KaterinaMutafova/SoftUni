from collections import deque

water = int(input())
queue = deque()

name = input()
while name != "Start":
    queue.append(name)
    name = input()

command = input()
while command != "End":
    command = command.split()
    if command[0] == "refill":
        water += int(command[1])
    else:
        litters = int(''.join(command))
        if litters <= water:
            water -= litters
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")

    command = input()

print(f"{water} liters left")



