gifts_to_buy = input().split(" ")
command = str

while command != "No Money":
    command = input()
    command_list = command.split()

    if "OutOfStock" in command_list:
        for i in range(len(gifts_to_buy)):
            if command_list[1] == gifts_to_buy[i]:
                gifts_to_buy[i] = "None"
    elif "Required" in command_list:
        index = int(command_list[2])
        if 0 <= index <= (len(gifts_to_buy)-1):
            gifts_to_buy[int(command_list[2])] = str(command_list[1])

    elif "JustInCase" in command_list:
        gifts_to_buy[-1] = command_list[1]

for m in gifts_to_buy:
    if "None" in gifts_to_buy:
        gifts_to_buy.remove("None")

for element in range(len(gifts_to_buy)):
    print(f"{gifts_to_buy[element]}", end=" ")




