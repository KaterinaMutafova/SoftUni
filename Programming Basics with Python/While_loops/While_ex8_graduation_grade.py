name = input()

year = 1
bad_grade = 0
sum_grades = 0


while year <= 12:
    grade = float(input())

    if grade < 4:
        bad_grade += 1
        if bad_grade == 2:
            break

        continue

    sum_grades += grade

    year += 1

if year == 13:
    year -=1

if bad_grade == 2:
    print(f"{name} has been excluded at {year} grade")
else:
    average_grade = sum_grades / year
    print(f"{name} graduated. Average grade: {average_grade:.2f}")

