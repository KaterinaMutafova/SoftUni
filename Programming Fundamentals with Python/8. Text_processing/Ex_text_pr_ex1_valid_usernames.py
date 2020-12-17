# Printing of only the valid usernames:
# import re
#
# username_string = input()
#
# pattern = r"(^|(?<=\s))[A-Za-z0-9_-]{3,16}($|(?=\s)|(?=\,))"
#
# valid_username = re.finditer(pattern, username_string)
#
# for word in valid_username:
#     print(word.group())


username_list = input().split(", ")
invalid_username = []

for word in username_list:
    if not (3 <= len(word) <= 16):
        invalid_username.append(word)
        continue
    for char in word:
        if char.isdigit() or char.isalpha() or char == "-" or char == "_":
            pass
        else:
            invalid_username.append(word)
    if "@" not in word:
        pass
    else:
        invalid_username.append(word)

for invalid_word in invalid_username:
    if invalid_word in username_list:
        username_list.remove(invalid_word)

for word in username_list:
    print(word)










