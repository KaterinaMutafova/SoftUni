#Първият ред съдържа час на изпита – цяло число от 0 до 23;
#Вторият ред съдържа минута на изпита – цяло число от 0 до 59;
#Третият ред съдържа час на пристигане – цяло число от 0 до 23;
#Четвъртият ред съдържа минута на пристигане – цяло число от 0 до 59.

exam_hour = int(input())
exam_min = int(input())
hour_arrival = int(input())
min_arrival = int(input())

total_min_exam = exam_min + exam_hour * 60
total_min_arrival = min_arrival + hour_arrival * 60
mm_diff = abs(total_min_exam - total_min_arrival)
hh = mm_diff // 60
mm = mm_diff % 60

if total_min_arrival < total_min_exam - 30:
    print("Early")
    if mm_diff <= 59:
        print(f"{mm_diff} minutes before the start")
    elif mm_diff > 59:
        if mm <= 9:
            print(f"{hh}:0{mm} hours before the start")
        elif mm > 9:
            print(f"{hh}:{mm} hours before the start")

elif total_min_exam >= total_min_arrival >= total_min_exam - 30:
    print("On time")
    if total_min_arrival != total_min_exam:
        print(f"{mm_diff} minutes before the start")


elif total_min_arrival > total_min_exam:
    print("Late")
    if mm_diff <= 59:
        print(f"{mm_diff} minutes after the start")
    elif mm_diff > 59:
        if mm <= 9:
            print(f"{hh}:0{mm} hours after the start")
        elif mm > 9:
            print(f"{hh}:{mm} hours after the start")










