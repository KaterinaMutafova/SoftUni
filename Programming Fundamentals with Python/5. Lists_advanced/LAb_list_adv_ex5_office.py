employee_happiness = input().split()
factor = int(input())

employee_happiness = list(map(lambda x: int(x) * factor, employee_happiness))

average_happiness = (sum(employee_happiness)) / (len(employee_happiness))

happy_employees = list(filter(lambda x: x >= (sum(employee_happiness) / len(employee_happiness)), employee_happiness))

if len(happy_employees) >= len(employee_happiness) / 2:
    print(f"Score: {len(happy_employees)}/{len(employee_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employee_happiness)}. Employees are not happy!")






