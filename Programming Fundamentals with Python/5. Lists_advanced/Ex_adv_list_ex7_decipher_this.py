def decipher_word(word):
    list_word = list(word)
    first_letter_digit = []
    the_end_of_word = []
    for i in range(len(list_word)):
        if list_word[i].isdigit():
            first_letter_digit.append(list_word[i])
        else:
            the_end_of_word.append(list_word[i])
    first_letter_digit = [chr(int("".join(first_letter_digit)))]
    final_list = first_letter_digit + the_end_of_word
    final_list[1], final_list[-1] = final_list[-1], final_list[1]
    final_list = "".join(final_list)
    return final_list


string_words = input().split(" ")
decoded_word = []
for j in string_words:
    decoded_word.append(decipher_word(j))

print(" ".join(decoded_word))


# x = chr(97) -->  a
# y = ord("a") -->  97
