number = int(input())

for i in range(1, number+1):
    for j in range(0, i):
        print("*", end="")
    print()

for l in range(number - 1, 0, -1):
    for j in range(0, l):
        print("*", end="")
    print()

