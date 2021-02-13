from collections import deque

def get_the_shortest_job(list_j):
    shortest_j = list_j[0]
    index_shortest_j = 0
    for index in range(len(list_j)):
        if list_j[index] < shortest_j and list_j[index] != 0:
            shortest_j = list_j[index]
            index_shortest_j = index
        elif list_j[index] == shortest_j:
            if index < index_shortest_j:
                shortest_j = list_j[index]
                index_shortest_j = index
        elif shortest_j == 0:
            shortest_j = list_j[index]
            index_shortest_j = index
    return shortest_j, index_shortest_j

list_jobs = deque([int(el) for el in input().split(", ")])

index_of_the_job = int(input())

job_at_index = list_jobs[index_of_the_job]

counter = 0

while not list_jobs[index_of_the_job] == 0:
    shortest_job, shortest_index = get_the_shortest_job(list_jobs)
    while not list_jobs[shortest_index] == 0:
        list_jobs[shortest_index] -= 1
        counter += 1

print(counter)





