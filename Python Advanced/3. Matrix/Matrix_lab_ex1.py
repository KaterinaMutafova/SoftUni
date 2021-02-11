def get_rows_and_cols(data_str):
    r, c = [int(num) for num in data_str.split(', ')]
    return r, c


rows, columns = get_rows_and_cols(input())
matrix = []
sum_matrix = 0

for row in range(rows):
    data = [int(el) for el in input().split(', ')]
    sum_matrix += sum(data)
    matrix.append(data)


print(sum_matrix)
print(matrix)




