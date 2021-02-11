def read_matrix(is_test = False):
    if is_test:
        return [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0],

        ]
    (rows_count, cols_count) = map(int, input().split(", "))

    matrix = []
    for row_index in range(rows_count):
        row = [int(el) for el in input().split(", ")]
        matrix.append(row)
    return matrix


def get_sub_matrix_sum(matrix, row_index, col_index, size):
    sum = matrix[row_index][col_index] + matrix[row_index][col_index + 1] + matrix[row_index + 1][col_index] + matrix[row_index + 1][col_index + 1]
    return sum


def get_best_sum(matrix, size):
    best_row_index = 0
    best_col_index = 0
    best_sum = get_sub_matrix_sum(matrix, 0, 0, size_submatrix)
    for index_r in range(len(matrix) - size_submatrix + 1):
        for index_c in range(len(matrix[index_r]) - size_submatrix + 1):
            current_sub_matrix_sum = get_sub_matrix_sum(matrix, index_r, index_c, size)
            if current_sub_matrix_sum > best_sum:
                best_sum = current_sub_matrix_sum
                best_row_index = index_r
                best_col_index = index_c

    return (best_row_index, best_col_index)


def print_result(matrix, row_i, col_i, size):
    for r in range(row_i, row_i + size):
        m =[]
        for c in range(col_i, col_i + size):
            m.append(matrix[r][c])
        print(' '.join([str(i)for i in m]))
    print(get_sub_matrix_sum(matrix, row_i, col_i, size))



matrix = read_matrix()
size_submatrix = 2

(best_row_index, best_col_index) = get_best_sum(matrix, size_submatrix)
best_sum = get_sub_matrix_sum(matrix, best_row_index, best_col_index, size_submatrix)

print_result(matrix, best_row_index, best_col_index, size_submatrix)

