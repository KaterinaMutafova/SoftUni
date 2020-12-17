employee_1_per_hour = int(input())
employee_2_per_hour = int(input())
employee_3_per_hour = int(input())
count_of_people = int(input())

list_efficiency = [employee_1_per_hour, employee_2_per_hour, employee_3_per_hour]
hours = 0

while count_of_people > 0:
    hours += 1
    count_of_people -= sum(list_efficiency)

    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")



# total_hours_without_breaks = count_of_people / sum(list_efficiency)
#
# print(total_hours_without_breaks)