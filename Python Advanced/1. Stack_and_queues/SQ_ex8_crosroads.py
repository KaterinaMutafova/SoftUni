from collections import deque

green_light_s = int(input())
free_window = int(input())

waiting_line = deque([])
counter = 0
is_crushed = False


while True:
    command = input()
    if command == "END":
        print("Everyone is safe.")
        print(f"{counter} total cars passed the crossroads.")
        break

    if command == "green":
        current_green_light_s = green_light_s
        current_free_window = free_window
        while True:
            current_car = waiting_line.popleft()
            counter += 1
            current_green_light_s -= len(current_car)
            if current_green_light_s > 0:
                if len(waiting_line) > 0:
                    continue
                break
            elif current_green_light_s == 0:
                break
            elif current_green_light_s < 0:
                diff_1 = abs(current_green_light_s)
                current_free_window -= diff_1
                if current_free_window >= 0:
                    break
                else:
                    is_crushed = True
                    hit_index = current_free_window
                    break
    else:
        car = command
        waiting_line.append(car)
    if is_crushed:
        print("A crash happened!")
        print(f"{current_car} was hit at {current_car[hit_index]}.")
        exit(0)







