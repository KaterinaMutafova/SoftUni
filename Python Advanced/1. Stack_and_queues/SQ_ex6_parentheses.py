parentheses = input()

is_balanced = True
dict_parentheses = {"(": ")", "{": "}", "[": "]"}


stack_open = []

for ch in parentheses:
    if ch in "({[":
        stack_open.append(ch)
    else:
        if not stack_open:
            is_balanced = False
            break
        last_open = stack_open.pop()
        if not dict_parentheses[last_open] == ch:
            is_balanced = False
            break

if is_balanced:
    print("YES")
else:
    print("NO")

