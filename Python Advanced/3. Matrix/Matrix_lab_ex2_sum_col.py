def get_rows_and_cols(data_str):
    r, c = [int(num) for num in data_str.split(', ')]
    return r, c


rows, columns = get_rows_and_cols(input())
matrix = []


for row in range(rows):
    data = [int(el) for el in input().split(' ')]
    matrix.append(data)

col_sum = 0

for big_i in range(columns):
    for small_i in range(rows):
        current_num = matrix[small_i][big_i]
        col_sum += current_num
    print(col_sum)
    col_sum = 0
