import sys

command = input()
minimum = sys.maxsize
number = 0

while command != "Stop":
    number = int(command)

    if number < minimum:
        minimum = number

    command = input()

print(minimum)
