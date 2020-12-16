# Широчина на свободното пространство - цяло число;
# Дължина на свободното пространство - цяло число;
# Височина на свободното пространство - цяло число;
# На следващите редове (до получаване на команда Done) - брой кашони, които се пренасят в
# квартирата - цели числа

width = int(input())
length = int(input())
height = int(input())
command = input()

#flag = False
size = width * length * height

while command != "Done":
    size -= int(command)

    if size <= 0:
        break

    command = input()

if size > 0:
    print(f"{size} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(size)} Cubic meters more.")




