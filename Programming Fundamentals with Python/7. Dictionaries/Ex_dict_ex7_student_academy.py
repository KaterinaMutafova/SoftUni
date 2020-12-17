rows = int(input())

students_dict = {}

for _ in range(rows):
    student_name = input()
    grade = float(input())
    if student_name not in students_dict:
        students_dict[student_name] = []
    students_dict[student_name].append(grade)

filtered_students = {}

for student, list_grades in students_dict.items():
    average_grade = sum(list_grades) / len(list_grades)
    if average_grade >= 4.50:
        filtered_students[student] = average_grade

filtered_students = sorted(filtered_students.items(), key=lambda x: x[1], reverse=True)
for student, grade in filtered_students:
    print(f"{student} -> {grade:.2f}")


