from collections import deque

count_pump = int(input())
que_pump = deque()

tank_petrol = 0
counter = 0

for i in range(count_pump):
    pump_info = input().split()
    que_pump.append(pump_info)

for i in range(count_pump):
    counter = i
    is_vaild = True
    for j in range(count_pump):
        tank_petrol += int(que_pump[j][0])
        if tank_petrol < int(que_pump[j][1]):
            tank_petrol = 0
            que_pump.append(que_pump.popleft())
            is_vaild = False
            break
        else:
            tank_petrol -= (int(que_pump[j][1]))
            if j == count_pump - 1:
                break

    if is_vaild:
        print(i)
        break



















