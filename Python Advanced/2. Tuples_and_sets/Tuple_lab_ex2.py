import math
count = int(input())

student_dict = {}

for stud in range(count):
    student_data = input().split(" ")
    name = student_data[0]
    grade = float(student_data[1])
    if name not in student_dict:
        student_dict[name] = []
    student_dict[name].append(grade)

for name, grades in student_dict.items():
    avg = sum(grades)/len(grades)
    marks = ' '.join(map(lambda grade: f'{grade:.2f}', grades))
    print(f"{name} -> {marks} (avg: {avg:.2f})")

