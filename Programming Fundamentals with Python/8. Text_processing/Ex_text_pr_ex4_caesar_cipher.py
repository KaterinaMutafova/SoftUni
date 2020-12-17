# Encrypt a message

line = input()

result = ""
for word in line:
    for index in range(len(word)):
        new_index = ord(word[index]) + 3
        new_letter = chr(new_index)
        result += new_letter

print(result)





