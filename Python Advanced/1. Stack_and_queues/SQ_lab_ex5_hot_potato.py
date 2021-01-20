from collections import deque

players = input().split(" ")
step = int(input())
people_list = deque(players)
counter = 0

while len(people_list) > 1:
    counter += 1
    current_player = people_list.popleft()
    if counter == step:
        print(f"Removed {current_player}")
        counter = 0
    else:
        people_list.append(current_player)

print(f"Last is {people_list.popleft()}")



