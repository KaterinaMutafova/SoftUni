hour = int(input())
minutes = int(input())

new_hour = hour
new_minutes = minutes + 15


if new_minutes > 59:
    new_minutes = new_minutes % 60
    new_hour = new_hour + 1

if new_hour > 23:
    new_hour = 0

if new_minutes > 9:
    print(f"{new_hour}:{new_minutes}")
else:
    print(f"{new_hour}:0{new_minutes}")

