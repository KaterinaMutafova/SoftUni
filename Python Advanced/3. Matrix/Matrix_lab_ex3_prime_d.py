rows_cols = int(input())
matrix = []


for row in range(rows_cols):
    data = [int(el) for el in input().split(' ')]
    matrix.append(data)

sum_d = 0
for i in range(rows_cols):
    sum_d += matrix[i][i]

print(sum_d)
