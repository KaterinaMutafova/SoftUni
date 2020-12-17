line = input().split()
str1 = line[0]
str2 = line[1]

max_chars = max(len(str1), len(str2))
min_chars = min(len(str1), len(str2))

sum_1 = 0
sum_2 = 0

if len(str1) == max_chars:
    max_word = str1
    min_word = str2
else:
    max_word = str2
    min_word = str1

for index in range(min_chars):
    sum_1 += (ord(str1[index]) * ord(str2[index]))

for ind in range(min_chars, max_chars):
    sum_2 += ord(max_word[ind])

sum = sum_1 + sum_2

print(sum)