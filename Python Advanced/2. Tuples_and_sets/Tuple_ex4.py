def get_dictionary(word):
    dict_word = {}
    for ch in word:
        if ch not in dict_word:
            dict_word[ch] = 1
        else:
            dict_word[ch] += 1
    return dict_word


def get_result(dict_word):
    dict_word = sorted(dict_word.items(), key=lambda x: x[0], reverse=False)
    for key, value in dict_word:
        print(f"{key}: {value} time/s")


text = input()
text_dict = get_dictionary(text)
get_result(text_dict)