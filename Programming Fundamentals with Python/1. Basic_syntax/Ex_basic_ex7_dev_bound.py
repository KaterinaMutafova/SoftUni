divisor = int(input())
bound = int(input())

for N in range(bound, 0, -1):
    if N % divisor == 0 and N != 0:
        print(N)
        break

