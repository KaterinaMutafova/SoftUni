character_1 = input()
character_2 = input()


def character_in_between(first_char, second_char):
    number_1 = ord(first_char)
    number_2 = ord(second_char)
    result = ""
    for number in range(number_1 + 1, number_2):
        result += str(chr(number)) + " "
    return result


print(character_in_between(character_1, character_2))



# # result_1 = chr(int(character_1))      # from num ---> ascci table character
# result_2 = ord(character_2)         # from character ----> number
