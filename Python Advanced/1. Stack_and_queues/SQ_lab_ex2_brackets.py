text = input()
bracket_list = []

for i in range(len(text)):
    if text[i] == "(":
        bracket_list.append(i)
    elif text[i] == ")":
        start_index = bracket_list.pop()
        print(text[start_index:i + 1])

