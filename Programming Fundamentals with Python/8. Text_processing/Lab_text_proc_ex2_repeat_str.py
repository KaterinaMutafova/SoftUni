# Repeat a  list of strings a certain number of  times:

result = ""
string_line = input().split()

for word in string_line:
    result += word * len(word)

print(result)