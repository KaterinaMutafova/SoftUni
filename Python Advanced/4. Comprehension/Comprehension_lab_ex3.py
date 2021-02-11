count_rows = int(input())

matrix = []
for i in range(count_rows):
    line = [int(el) for el in input().split(", ")]
    matrix.append(line)

matrix = [list(filter((lambda x: x % 2 == 0), matrix[i])) for i in range(len(matrix))]


print(matrix)