box = list(map(int, input().split(" ")))

CAPACITY = int(input())

current_capacity_index = CAPACITY
counter = 1

while box:
    current_cloth = box.pop()
    if current_cloth <= current_capacity_index:
        current_capacity_index -= current_cloth
    elif current_cloth > current_capacity_index:
        counter += 1
        current_capacity_index = CAPACITY
        current_capacity_index -= current_cloth

print(counter)















