SNAKE = "S"
FOOD = "*"
BURROW = "B"
EMPTY_FIELD = "-"
PASSED_FIELD = "."


def get_board():
    board = []
    count_rows = int(input())
    for r in range(count_rows):
        line = list(input())
        board.append(line)
    return board


def find_snake(board):
    row_index_s = ""
    col_index_s = ""
    for row in range(len(board)):
        if SNAKE in board[row]:
            row_index_s = row
            col_index_s = board[row].index(SNAKE)
    return (row_index_s, col_index_s)


def find_burrows(board):
    burrows_indexes = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == BURROW:
                burrows_indexes.append([row, col])
    return burrows_indexes


def find_food(board):
    food_indexes = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == FOOD:
                food_indexes.append([row, col])
    return food_indexes


def in_range(value, max_value):
    return 0 <= value < max_value


def get_to_the_other_burrow(board, next_r, next_c, burrows):
    next_row_s = ""
    next_col_s = ""
    for burrow in burrows:
        if burrow == [next_r, next_c]:
            burrows.remove(burrow)
    next_row_s = burrows[0][0]
    next_col_s = burrows[0][1]
    return (next_row_s, next_col_s)


def print_result(game_won, game_lost):
    if game_won:
        print("You won! You fed the snake.")
    elif game_lost:
        print("Game over!")
    print(f"Food eaten: {food_quantity}")


def print_matrix(board):
    for row in board:
        print(''.join(row))




board = get_board()
snake_position = find_snake(board)
burrows_position = find_burrows(board)
food_position = find_food(board)

food_quantity = 0

count_rows = len(board)
count_columns = len(board[0])
game_lost = False
game_won = False

commands = {"up": (-1, 0), "down": (+1, 0), "right": (0, +1), "left": (0, -1)}
while True:
    if game_lost:
        break
    if food_quantity >= 10:
        game_won = True
        break

    command = input()
    next_move_row = snake_position[0] + commands[command][0]
    next_move_col = snake_position[1] + commands[command][1]
    if in_range(next_move_row, count_rows) and in_range(next_move_col, count_columns):
        if board[next_move_row][next_move_col] == FOOD:
            food_quantity += 1
            board[snake_position[0]][snake_position[1]] = PASSED_FIELD
            snake_position = (next_move_row, next_move_col)
            board[next_move_row][next_move_col] = SNAKE
            if food_quantity >= 10:
                game_won = True
                break
        elif board[next_move_row][next_move_col] == EMPTY_FIELD or board[next_move_row][next_move_col] == PASSED_FIELD:
            board[snake_position[0]][snake_position[1]] = PASSED_FIELD
            snake_position = (next_move_row, next_move_col)
            board[next_move_row][next_move_col] = SNAKE
        elif board[next_move_row][next_move_col] == BURROW:
            board[snake_position[0]][snake_position[1]] = PASSED_FIELD
            board[next_move_row][next_move_col] = PASSED_FIELD
            snake_position = get_to_the_other_burrow(board, next_move_row, next_move_col, burrows_position)
            board[snake_position[0]][snake_position[1]] = SNAKE

    else:
        board[snake_position[0]][snake_position[1]] = PASSED_FIELD
        game_lost = True


print_result(game_won, game_lost)
print_matrix(board)








