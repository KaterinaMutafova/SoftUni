BOMB = "*"
EMPTY_FIELD = "-"

def get_board():
    number_of_fields = int(input())
    board = []
    for i in range(number_of_fields):
        line = [EMPTY_FIELD] * number_of_fields
        board.append(line)
    return board


def get_mines():
    number_of_mines = int(input())
    mine_indexes = []
    for _ in range(number_of_mines):
        mine_index = input()
        mine_indexes.append(mine_index)
    return mine_indexes


def mark_mines(board, mines):
    for index_mine in mines:
        mine_row = int(index_mine[1])
        mine_col = int(index_mine[4])
        board[mine_row][mine_col] = BOMB

    return board


def in_range(value, max_value):
    return 0 <= value < max_value



def get_count_mines(board, row_i, col_i):
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

    fields_around = []
    for delta in deltas:
        row_index = row_i + delta[0]
        column_index = col_i + delta[1]
        if in_range(row_index, rows_count) and in_range(column_index, columns_count):
            field = board[row_index][column_index]
            fields_around.append(field)

    count_mines = 0

    for field in fields_around:
        if field == BOMB:
            count_mines += 1

    return count_mines


def print_board(board):
    for r in board:
        result = [str(el) for el in r]
        print(' '.join(result))



board = get_board()
mines = get_mines()
board = mark_mines(board, mines)

for r in range(len(board)):
    for c in range(len(board[0])):
        if not board[r][c] == BOMB:
            board[r][c] = get_count_mines(board, r, c)


print_board(board)
