pirate_ship = input()
war_ship = input()
max_health = int(input())
is_stalemate = True


pirate_ship = list(map(int, pirate_ship.split(">")))
war_ship = list(map(int, war_ship.split(">")))

# •	Fire {index} {damage}
# •	Defend {startIndex} {endIndex} {damage}
# •	Repair {index} {health}
# •	Status

section_for_repair_p = []

command = input()

while not command == "Retire":
    if not is_stalemate:
        break
    command = command.split()

    if command[0] == "Fire":
        index_w = int(command[1])
        damage_w = int(command[2])
        if 0 <= index_w < len(war_ship):
            war_ship[index_w] -= damage_w
            if war_ship[index_w] <= 0:
                print("You won! The enemy ship has sunken.")
                is_stalemate = False
                break
        else:
            pass
        if not is_stalemate:
            break

    elif command[0] == "Defend":
        start_index_p = int(command[1])
        end_index_p = int(command[2])
        damage_p = int(command[3])
        for sec in range(start_index_p, end_index_p + 1):
            pirate_ship[sec] -= damage_p
            if pirate_ship[sec] <= 0:
                print("You lost! The pirate ship has sunken.")
                is_stalemate = False
                break
        if not is_stalemate:
            break

    elif command[0] == "Repair":
        index_p = int(command[1])
        health = int(command[2])
        if 0 <= index_p < len(pirate_ship):
            if pirate_ship[index_p] + health <= max_health:
                pirate_ship[index_p] += health
            else:
                pirate_ship[index_p] = max_health
        else:
            pass

    elif command[0] == "Status":
        section_for_repair_value = 0.20 * max_health
        for section in pirate_ship:
            if section < section_for_repair_value:
                section_for_repair_p.append(section)
        count_sections_for_repair = len(section_for_repair_p)
        print(f"{count_sections_for_repair} sections need repair.")

    command = input()


if command == "Retire" and is_stalemate:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")





    
# НЕДОВЪРШЕН ВАРИАНТ!!!
#
#
# НЕДОВЪРШЕН ВАРИАНТ!!!!
#
# def fire_command(war_ship_list, index, damage):
#     if 0 <= index < len(war_ship_list):
#         war_ship_list[index] -= damage
#         if war_ship_list[index] <= 0:
#             is_stalemate = False
#             print("You won! The enemy ship has sunken.")
#         else:
#             return war_ship_list
#
#
# def defend_command(pirate_ship_list, index_1, index_2, damage):
#     for sec in range(index_1, index_2 + 1):
#         pirate_ship_list[sec] -= damage
#         if pirate_ship_list[sec] <= 0:
#             print("You lost! The pirate ship has sunken.")
#             is_stalemate = False
#             break
#         else:
#             return pirate_ship_list
#
#
# def repair_command(pirate_ship_list, index, health_value, max_health_value):
#     if 0 <= index < len(pirate_ship_list):
#         if pirate_ship_list[index] + health_value <= max_health_value:
#             pirate_ship_list[index] += health_value
#             return pirate_ship_list
#         else:
#             pirate_ship_list[index] = max_health_value
#             return pirate_ship_list
#
# def status_command(pirate_ship_list, max_health_value):
#     section_for_repair_value = 0.20 * max_health_value
#     for section in pirate_ship_list:
#         if section < section_for_repair_value:
#             section_for_repair_p.append(section)
#     count_sections_for_repair = len(section_for_repair_p)
#     return f"{count_sections_for_repair} sections need repair."
#
#
# pirate_ship = input()
# war_ship = input()
# max_health = int(input())
# is_stalemate = True
#
#
# pirate_ship = list(map(int, pirate_ship.split(">")))
# war_ship = list(map(int, war_ship.split(">")))
#
# # •	Fire {index} {damage}
# # •	Defend {startIndex} {endIndex} {damage}
# # •	Repair {index} {health}
# # •	Status
#
# section_for_repair_p = []
#
# command = input()
#
# while not command == "Retire":
#     if not is_stalemate:
#         break
#     command = command.split()
#
#     if command[0] == "Fire":
#         index_w = int(command[1])
#         damage_w = int(command[2])
#         fire_command(war_ship, index_w, damage_w)
#         if not is_stalemate:
#             break
#
#     elif command[0] == "Defend":
#         start_index_p = int(command[1])
#         end_index_p = int(command[2])
#         damage_p = int(command[3])
#         defend_command(pirate_ship, start_index_p, end_index_p, damage_p)
#         if not is_stalemate:
#             break
#
#     elif command[0] == "Repair":
#         index_p = int(command[1])
#         health = int(command[2])
#         repair_command(pirate_ship, index_p, health, max_health)
#
#     elif command[0] == "Status":
#         print(status_command(pirate_ship, max_health))
#
#     command = input()
#
#
# if command == "Retire" and is_stalemate:
#     print(f"Pirate ship status: {sum(pirate_ship)}")
#     print(f"Warship status: {sum(war_ship)}")
