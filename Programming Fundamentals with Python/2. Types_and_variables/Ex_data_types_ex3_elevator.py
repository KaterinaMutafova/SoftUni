num_people = int(input())
el_capacity = int(input())
additional = num_people % el_capacity

if additional < el_capacity and additional != 0:
    additional = 1

course = num_people // el_capacity + additional

print(course)