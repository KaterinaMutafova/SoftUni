first_sec = int(input())
second_sec = int(input())
third_sec = int(input())

total_sec = first_sec + second_sec + third_sec

total_minutes = total_sec // 60
left_sec = total_sec % 60

if left_sec > 9:
    print(f"{total_minutes}:{left_sec}")
else:
    print(f"{total_minutes}:0{left_sec}")






