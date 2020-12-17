string_words = input()

list_words = string_words.split(" ")

dict_letters = {}

for word in list_words:
    for letter in word:
        if letter not in dict_letters:
            dict_letters[letter] = 1
        else:
            dict_letters[letter] += 1

for (key,value) in dict_letters.items():
    print(f"{key} -> {value}")
