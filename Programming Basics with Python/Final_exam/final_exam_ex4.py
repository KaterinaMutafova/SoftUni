#  N – цяло число – 0 <= N < M
#  M – цяло число – N < M <= 10000
#  S – цяло числo – N <= S <= M

N = int(input())
M = int(input())
S = int(input())

while M != N:
    if M % 2 == 0 and M % 3 == 0:
        if S == M:
            break
        else:
            print(f"{M}", end=" ")

    M -= 1
















