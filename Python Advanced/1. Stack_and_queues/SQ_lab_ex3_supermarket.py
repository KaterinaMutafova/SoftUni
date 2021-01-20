from collections import deque

queue_list = deque()

while True:
    name = input()
    if name == "Paid":
        while len(queue_list):
            print(queue_list.popleft())
    elif name == "End":
        print(f"{len(queue_list)} people remaining.")
        break
    else:
        queue_list.append(name)



