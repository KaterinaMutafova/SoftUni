n = int(input())
counter_2 = 0
total_sum_average_marks = 0
total_average_marks = 0
name_presentation = input()

while name_presentation != "Finish":
    sum_mark = 0
    average_mark = 0
    to_print = False
    counter = 0
    while counter <= n:
        counter += 1
        mark = float(input())
        sum_mark += mark
        if to_print:
            break
        if counter == n:
            average_mark = sum_mark / n
            to_print = True
            if to_print:
                print(f"{name_presentation} - {average_mark:.2f}.")
                break
    counter_2 += 1
    total_sum_average_marks += average_mark
    name_presentation = input()

if name_presentation == "Finish":
    total_average_marks = total_sum_average_marks / counter_2
    print(f"Student's final assessment is {total_average_marks:.2f}.")



