characters_list = input().split(", ")

dict_numbers = {}
for el in characters_list:
    dict_numbers[el] = ord(el)



print(dict_numbers)
