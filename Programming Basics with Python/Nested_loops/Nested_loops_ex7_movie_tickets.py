# На първия ред до получаване на командата &quot;Finish&quot; - име на филма – текст
# На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
# За всеки филм, се чете по един ред до изчерпване на свободните места в залата или до получаване на
# командата &quot;End&quot;:
# Типа на закупения билет - текст (&quot;student&quot;, &quot;standard&quot;, &quot;kid&quot;)
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
count_movie_tickets = 0
total_tickets = 0
percent = 0

line = input()
while line != "Finish":
    name_movie = line
    free_seats = int(input())
    count_movie_tickets = 0

    line_2 = input()
    while line_2 != "End":
        type_ticket = line_2
        count_movie_tickets += 1
        if type_ticket == "student":
            student_tickets += 1
        elif type_ticket == "standard":
            standard_tickets += 1
        elif type_ticket == 'kid':
            kid_tickets += 1
        if count_movie_tickets == free_seats:
            break
        line_2 = input()
    total_tickets = student_tickets + standard_tickets + kid_tickets
    percent = (count_movie_tickets / free_seats) * 100
    print(f"{name_movie} - {percent:.2f}% full.")
    line = input()
percent_student = (student_tickets / total_tickets) * 100
percent_standard = (standard_tickets / total_tickets) * 100
percent_kids = (kid_tickets / total_tickets) * 100
print(f"Total tickets: {total_tickets}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kids:.2f}% kids tickets.")