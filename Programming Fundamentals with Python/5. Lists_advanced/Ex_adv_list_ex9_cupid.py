neighborhood_list = input().split("@")
neighborhood_list = [int(el) for el in neighborhood_list]

jump_command = input()

counter_houses = 0

while not jump_command == "Love!":
    jump, value = jump_command.split()
    value = int(value)
    counter_houses += value
    if counter_houses < len(neighborhood_list):
        if neighborhood_list[counter_houses] == 0:
            print(f"Place {counter_houses} already had Valentine's day.")
        elif neighborhood_list[counter_houses] > 0:
            neighborhood_list[counter_houses] -= 2
            if neighborhood_list[counter_houses] == 0:
                print(f"Place {counter_houses} has Valentine's day.")
    elif counter_houses >= len(neighborhood_list):
        counter_houses = 0
        if neighborhood_list[counter_houses] == 0:
            print(f"Place {counter_houses} already had Valentine's day.")
        elif neighborhood_list[counter_houses] > 0:
            neighborhood_list[counter_houses] -= 2
            if neighborhood_list[counter_houses] == 0:
                print(f"Place {counter_houses} has Valentine's day.")

    jump_command = input()

houses_without_valentines = []

for house in neighborhood_list:
    if not house == 0:
        houses_without_valentines.append(house)

print(f"Cupid's last position was {counter_houses}.")

if sum(neighborhood_list) == 0:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {len(houses_without_valentines)} places.")

# 8@2@4
# Jump 1
# Jump 3
# Jump 1
# Jump 3
# Jump 3
# Love!

