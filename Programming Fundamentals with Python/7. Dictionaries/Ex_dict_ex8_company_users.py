companies_dict = {}

company_data = input()
a = 6
while not company_data == "End":
    company, id_employee = company_data.split("->")
    if company not in companies_dict:
        companies_dict[company] = []
    if id_employee not in companies_dict[company]:
        companies_dict[company].append(id_employee)

    company_data = input()

companies_dict = sorted(companies_dict.items(), key=lambda x: x[0])

for company, employee in companies_dict:
    print(f"{company}")
    for e_id in employee:
        print(f"-- {e_id}")






