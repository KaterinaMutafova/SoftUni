def get_matrix():
    rows, cols = list(map(int, input().split(" ")))
    m = []
    for row in range(rows):
        line = list(map(int, input().split(" ")))
        m.append(line)
    return m


def get_sum_sub_matrix(m, r_i, c_i, size):
    sum_m = 0
    for r in range(r_i, r_i + size):
        for c in range(c_i, c_i + size):
            sum_m += m[r][c]
    return sum_m


def get_max_sum(matrix, size):
    max_sum = get_sum_sub_matrix(matrix, 0,0, size_submatrix)
    for row_i in range(len(matrix) - size + 1):
        for col_i in range(len(matrix[row_i]) - size + 1):
            current_sum = get_sum_sub_matrix(matrix, row_i, col_i, size)
            if current_sum > max_sum:
                max_sum = current_sum
                max_index_r = row_i
                max_index_c = col_i
    return (max_sum, max_index_r, max_index_c)



def print_result(matrix, max_r, max_col, max_sum, size):
    print(f"Sum = {max_sum}")
    for i in range(max_r, max_r + size):
        max_sub = []
        for j in range(max_col, max_col + size):
            print(matrix[i][j], end=" ")
        print()
        #     max_sub.append(matrix[i][j])
        # print(' '.join([str(t)for t in max_sub]))

size_submatrix = 3
matrix = get_matrix()
(max_sum, max_row_i, max_col_i) = get_max_sum(matrix, size_submatrix)
print_result(matrix, max_row_i, max_col_i, max_sum, size_submatrix)





