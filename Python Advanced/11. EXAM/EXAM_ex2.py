from math import floor

PLAYER = "P"
WALL = "X"


def get_matrix():
    size = int(input())
    matrix = []
    for row in range(size):
        line = input().split(" ")
        matrix.append(line)
    return matrix


def get_player_position(matrix):
    player_r = ""
    player_c = ""
    for row_index in range(len(matrix)):
        if PLAYER in matrix[row_index]:
            player_r = row_index
            player_c = matrix[row_index].index(PLAYER)
    return (player_r, player_c)


def in_range(value, max_value):
    return 0 <= value < max_value



matrix = get_matrix()
player_row, player_column = get_player_position(matrix)

player_coins = 0

rows_count = len(matrix)
columns_count = len(matrix[0])
game_lost = False
game_won = False



movements = {"up": (-1, 0), "right": (0, +1), "down": (+1, 0), "left": (0, -1)}
path_list = []

while True:
    if game_lost or game_won:
        break
    if player_coins >= 100:
        game_won = True
        break

    movement = input()
    if movement in movements:
        next_row_index = player_row + movements[movement][0]
        next_column_index = player_column + movements[movement][1]
        if in_range(next_row_index, rows_count) and in_range(next_column_index, columns_count):
            player_row = next_row_index
            player_column = next_column_index
            if not matrix[player_row][player_column] == WALL:
                path_list.append([player_row, player_column])
                coins_to_add = int(matrix[player_row][player_column])
                player_coins += coins_to_add
                if player_coins >= 100:
                    game_won = True
                    break

            elif matrix[player_row][player_column] == WALL:
                game_lost = True
                player_coins = player_coins * 0.50
                break

        else:
            game_lost = True
            player_coins = player_coins * 0.50
            break
    else:
        continue


if game_won:
    print(f"You won! You've collected {floor(player_coins)} coins.")
elif game_lost:
    print(f"Game over! You've collected {floor(player_coins)} coins.")

print("Your path:")
for move in path_list:
    print(move)




