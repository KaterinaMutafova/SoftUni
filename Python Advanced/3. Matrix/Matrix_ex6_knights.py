KNIGHT = "K"
EMPTY_FIELD = "0"

def get_matrix():
    size = int(input())
    matrix = []
    for row in range(size):
        line = list(input())
        matrix.append(line)
    return matrix


def find_knights(matrix):
    k_indexes = []
    for r_index in range(len(matrix)):
        for c_index in range(len(matrix[0])):
            if matrix[r_index][c_index] == KNIGHT:
                k_indexes.append([r_index, c_index])
    return k_indexes


def in_range(value, max_value):
    return 0 <= value < max_value


def check_knight(matrix, knight_index):
    deltas = [
        (-1, -2),
        (-2, -1),
        (-2, +1),
        (-1, +2),
        (+1, +2),
        (+2, +1),
        (+2, -1),
        (+1, -2),
    ]
    count_rows = len(matrix)
    count_columns = len(matrix[0])
    k_captures = 0

    for delta in deltas:
        new_k_row = knight_index[0] + delta[0]
        new_k_col = knight_index[1] + delta[1]
        if in_range(new_k_row, count_rows) and in_range(new_k_col, count_columns):
            if matrix[new_k_row][new_k_col] == KNIGHT:
                k_captures += 1
    return k_captures


def find_best_warrior_knight(matrix, k_indexes):
    count_best_captures = 0
    best_k_row_index = ""
    best_k_col_index = ""
    for knight_i in k_indexes:
        count_knight_captures = check_knight(matrix, knight_i)
        if count_knight_captures > count_best_captures:
            count_best_captures = count_knight_captures
            [best_k_row_index, best_k_col_index] = knight_i
    if not count_best_captures == 0:
        return [best_k_row_index, best_k_col_index]
    else:
        return None


def remove_best_warrior(matrix, best_w_row, best_w_col):
    matrix[best_w_row][best_w_col] = EMPTY_FIELD
    return matrix


matrix = get_matrix()
knight_indexes = find_knights(matrix)
count_removed_knights = 0
while True:
    if find_best_warrior_knight(matrix, knight_indexes):
        best_warrior_row, best_warrior_col = find_best_warrior_knight(matrix,knight_indexes)
        board = remove_best_warrior(matrix, best_warrior_row, best_warrior_col)
        knight_indexes.remove([best_warrior_row, best_warrior_col])
        count_removed_knights += 1
    else:
        break

print(count_removed_knights)
