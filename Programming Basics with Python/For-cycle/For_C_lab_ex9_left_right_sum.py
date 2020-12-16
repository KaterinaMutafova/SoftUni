n = int(input())

left_sum = 0
right_sum = 0

for i in range(n):
    num_1 = int(input())
    left_sum += num_1

for i in range(n):
    num_2 = int(input())
    right_sum += num_2

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")

