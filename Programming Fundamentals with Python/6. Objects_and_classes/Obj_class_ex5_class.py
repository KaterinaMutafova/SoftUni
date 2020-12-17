class Class:
    __students_count = 22
    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []
        self.counter = 0

    def add_student(self, name, grade):
        self.counter += 1
        if self.counter < 22:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        average_grade = float(sum(self.grades) / len(self.students))
        return average_grade

    def __repr__(self):
        name_of_students = ", ".join(self.students)
        result = f"The students in {self.name}: {name_of_students}. Average grade: {self.get_average_grade():.2f}"
        return result

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
