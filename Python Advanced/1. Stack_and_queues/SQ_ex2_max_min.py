# 1 – Push the element x into the stack.
# 2 – Delete the element present at the top of the stack.
# 3 – Print the maximum element in the stack.
# 4 – Print the minimum element in the stack.


def pushing1(s, num):
    s = s.append(int(command[1]))
    return s


def delete2(s):
    if len(s) > 0:
        s = s.pop()
        return s
    else:
        return s


def print_max(s):
    if len(s) > 0:
        max_num = max(s)
        print(max_num)


def print_min(s):
    if len(s) > 0:
        min_num = min(s)
        print(min_num)


n = int(input())

stack = []

for query in range(n):
    command = input().split(" ")
    if command[0] == "1":
        number = int(command[1])
        pushing1(stack, number)
    elif command[0] == "2":
        delete2(stack)
    elif command[0] == "3":
        print_max(stack)
    elif command[0] == "4":
        print_min(stack)

stack_back = []
result = ""

length = len(stack)

for ch in range(length):
    if ch == length - 1:
        result += str(stack.pop())
    else:
        result += str(stack.pop()) + ", "

print(result)





