import sys
n = int(input())
current_max = -sys.maxsize
current_min = sys.maxsize

for i in range(0,n):
    num = int(input())
    if num > current_max:
        current_max = num
    if num < current_min:
        current_min = num

print(f"Max number: {current_max}")
print(f"Min number: {current_min}")

