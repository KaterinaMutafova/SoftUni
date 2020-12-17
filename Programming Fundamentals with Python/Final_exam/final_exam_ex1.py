def change_func(string_info, old_char_to_replace, new_char):
    string_info = string_info.replace(old_char_to_replace, new_char)
    return string_info


def find_word_func(string_info, searched_word):
    if searched_word in string_info:
        return True
    else:
        return False


def ends_with_func(string_info, searched_word):
    if string_info.endswith(searched_word):
        return True
    else:
        return False

def cut_func(string_info, start_index, length_info):
    end_index = start_index + length_info
    result_string = ""
    for index_el in range(start_index, end_index):
        result_string += string_info[index_el]
    string_info = result_string
    return string_info


string_line = input()

command = input()
a = 6
while not command == "Done":
    command_data = command.split()
    if command_data[0] == "Change":
        character_to_replace = command_data[1]
        new_character = command_data[2]
        string_line = change_func(string_line, character_to_replace, new_character)
        print(string_line)
    elif command_data[0] == "Includes":
        word_to_find = command_data[1]
        print(find_word_func(string_line, word_to_find))

    elif command_data[0] == "End":
        word_to_find = command_data[1]
        print(ends_with_func(string_line, word_to_find))

    elif command_data[0] == "Uppercase":
        string_line = string_line.upper()
        print(string_line)

    elif command_data[0] == "FindIndex":
        char_to_search = command_data[1]
        for index in range(len(string_line)):
            letter_in_string = string_line[index]
            if letter_in_string == char_to_search:
                print(index)
                break

    elif command_data[0] == "Cut":
        start_i = int(command_data[1])
        length = int(command_data[2])
        print(cut_func(string_line, start_i, length))

    command = input()








# //Th1s 1s my str1ng!//
# Change 1 i
# Includes string
# End my
# Uppercase
# FindIndex I
# Cut 5 5
# Done
