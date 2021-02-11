def get_matrix():
    rows, cols = list(map(int, input().split(" ")))

    m = []
    for r in range(rows):
        line = input().split(" ")
        m.append(line)
    return m


def check_index(matrix, row_i, col_i, is_found=False):
    if matrix[row_i][col_i] == matrix[row_i][col_i + 1]:
        if matrix[row_i][col_i + 1] == matrix[row_i + 1][col_i]:
            if matrix[row_i + 1][col_i] == matrix[row_i + 1][col_i + 1]:
                is_found = True

    return is_found


def get_count_sub_matrix(matrix, size_submatrix):
    counter = 0
    for r in range(len(matrix) - size_submatrix + 1):
        for c in range(len(matrix[r]) - size_submatrix + 1):
            if check_index(matrix, r, c, is_found):
                counter += 1
    return counter


matrix = get_matrix()

is_found = False
size_submatrix = 2

counter = get_count_sub_matrix(matrix, size_submatrix)

print(counter)




