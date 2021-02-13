EMPTY_SQUARE = "."
QUEEN = "Q"
KING = "K"


def get_board():
    board = []
    for _ in range(8):
        line = input().split(" ")
        board.append(line)
    return board


def find_king(board):
    king_l = []
    king_r = ""
    king_c = ""
    for king_r in range(len(board)):
        # for c in range(len(board[r])):
        #     if board[r][c] == KING:
        #         king_r = r
        #         king_c = c
        #         return king_r, king_c
        if KING in board[king_r]:
            king_c = board[king_r].index(KING)
            return king_r, king_c


def in_range(value, max_value):
    return 0 <= value < max_value


def search_with_deltas(board, king_r, king_c, delta):
    rows_count = len(board)
    columns_count = len(board[0])
    (delta_row, delta_column) = delta
    row_index, col_index = king_r, king_c

    while True:
        if not in_range(row_index, rows_count) or not in_range(col_index, columns_count):
            return None
        if board[row_index][col_index] == QUEEN:
            return [row_index, col_index]
        row_index += delta_row
        col_index += delta_column



def check_for_killer_queens(board, king_row, king_col):
    rows_count = len(board)
    columns_count = len(board[0])

    deltas = [
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, +1),
        (0, +1),
        (+1, +1),
        (+1, 0),
        (+1, -1),
    ]

    killer_queens_indexes = [
        search_with_deltas(board, king_row, king_col, delta) for delta in deltas

    ]
    return [queen for queen in killer_queens_indexes if queen]


def print_result(killer_queens_indexes):
    if killer_queens_indexes:
        for queen_index in killer_queens_indexes:
            print(queen_index)
    else:
        print("The king is safe!")



board = get_board()
king_row, king_col = find_king(board)


killer_queens_indexes = check_for_killer_queens(board, king_row, king_col)

print_result(killer_queens_indexes)


