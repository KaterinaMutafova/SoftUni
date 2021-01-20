from collections import deque


def check_max(num,current_max):
    if num > current_max:
        current_max = num
    return current_max


food_supply = int(input())

orders = [int(el) for el in input().split(" ")]

order_que = deque(orders)
max_order = 0

if order_que:
    for client in order_que:
        max_order = check_max(client, max_order)

print(max_order)


while order_que:
    current_client = order_que.popleft()
    if current_client > food_supply:
        order_que.appendleft(current_client)
        break
    food_supply -= current_client


if order_que:
    left_orders = " ".join(map(str, order_que))
    print(f"Orders left: {left_orders}")
else:
    print("Orders complete")



