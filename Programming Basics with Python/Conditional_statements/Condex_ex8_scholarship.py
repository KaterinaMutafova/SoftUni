#1. Доход в лева - реално число;
#2. Среден успех - реално числсо;
#3. Минимална работна заплата – реално число.
from math import floor
income = float(input())
average_grades = float(input())
minimum_salary = float(input())

social_scholarship = 0
excellent_scholarship = 0

if average_grades >= 5.50 and income < minimum_salary:
    excellent_scholarship = average_grades * 25
    social_scholarship = minimum_salary * 0.35
    if excellent_scholarship >= social_scholarship:
        print(f"You get a scholarship for excellent results {floor(excellent_scholarship)} BGN")
    else:
        social_scholarship = minimum_salary * 0.35
        print(f"You get a Social scholarship {floor(social_scholarship)} BGN")

elif average_grades >= 5.50:
    excellent_scholarship = average_grades * 25
    print(f"You get a scholarship for excellent results {floor(excellent_scholarship)} BGN")

elif average_grades >= 4.50 and income < minimum_salary:
    social_scholarship = minimum_salary * 0.35
    print(f"You get a Social scholarship {floor(social_scholarship)} BGN")

elif average_grades < 4.50 or income > minimum_salary:
    print("You cannot get a scholarship!")
