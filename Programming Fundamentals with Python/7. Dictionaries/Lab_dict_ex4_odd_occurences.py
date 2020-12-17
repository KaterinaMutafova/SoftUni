words = input().split(" ")

dict = {}

for word in words:
    lower_word = word.lower()
    if lower_word not in dict:
        dict[lower_word] = 0
    dict[lower_word] += 1

for (key, value) in dict.items():
    if value % 2 != 0:
        print(key, end=" ")
