#На първи ред - брой незадоволителни оценки - цяло число;
#След това многократно се четат по два реда:
#Име на задача – текст;
#Оценка - цяло число в интервала [2…6]

count_poor_marks = int(input())

current_count_poor_marks = 0
count_marks = 0
sum_marks = 0


command = input()

while command != "Enough":
    problem = command
    mark = int(input())
    sum_marks += mark
    count_marks += 1

    if mark <= 4:
        current_count_poor_marks += 1
        if current_count_poor_marks == count_poor_marks:
            print(f"You need a break, {current_count_poor_marks} poor grades.")
            break

    command = input()


if command == "Enough":
    average_mark = sum_marks / count_marks
    print(f"Average score: {average_mark:.2f}")
    print(f"Number of problems: {count_marks}")
    print(f"Last problem: {problem}")



