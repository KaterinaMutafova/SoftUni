index_1 = int(input())
index_2 = int(input())

num_diff = index_2 - index_1

for i in range(0,num_diff + 1):
    print(chr(index_1 + i), end=" ")

