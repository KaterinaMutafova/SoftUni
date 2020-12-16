import sys
command = input()

maximum = -sys.maxsize
number = 0

while command != "Stop":
    number = int(command)

    if number > maximum:
        maximum = number

    command = input()

print(maximum)




