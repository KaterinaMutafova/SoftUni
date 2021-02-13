from collections import deque

customers = [int(el) for el in input().split(", ")]
taxis = [int(t) for t in input().split(", ")]

customers = deque(customers)
total_time = 0

while not len(taxis) == 0:
    if taxis[-1] >= customers[0]:
        total_time += customers[0]
        taxis.pop()
        customers.popleft()
    elif taxis[-1] < customers[0]:
        taxis.pop()
    if len(customers) == 0:
        break

if len(customers) == 0:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(c) for  c in customers)}")





