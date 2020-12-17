students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())

max_bonus_points = 0
attendances_for_student_with_max_bonus = 0


for student in range(students_count):
    attendance_num_for_stud = int(input())
    current_student_bonus = attendance_num_for_stud / lectures_count * (5 + additional_bonus)
    if current_student_bonus > max_bonus_points:
        max_bonus_points = current_student_bonus
        attendances_for_student_with_max_bonus = attendance_num_for_stud

print(f"Max Bonus: {round(max_bonus_points)}.")
print(f"The student has attended {attendances_for_student_with_max_bonus} lectures.")


