courses_dict = {}

course_data = input()

while not course_data == "end":
    course_data = course_data.split(" : ")
    course = course_data[0]
    student = course_data[1]
    if course not in courses_dict:
        courses_dict[course] = {"students": [], "count": 0}
    courses_dict[course]['students'].append(student)
    courses_dict[course]['count'] += 1

    course_data = input()

sorted_dict = sorted(courses_dict.items(), key=lambda x: x[1]['count'], reverse=True)


for course, students_data in sorted_dict:
    print(f"{course}: {students_data['count']}")
    sorted_students = sorted(students_data['students'])
    for student in sorted_students:
        print(f"-- {student}")









