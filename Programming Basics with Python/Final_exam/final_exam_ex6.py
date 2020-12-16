#Първоначално от конзолата се прочита броя на авиокомпаниите – цяло число в интервала [1… 20]
#След това за всяка авиокомпания се прочита:
# Името на авиокомпанията – текст
# До получаване на командата "Finish" се чете:
#o Брой пътници на полет – цяло число в интервала [1... 360]

from math import floor
company_number = int(input())
most_pass_per_flight = 0
current_most_pass_per_flight = 0
best_company = ""
current_best_company = ""

for i in range(1, company_number + 1):
    air_company_name = input()
    counter = 0
    sum_passengers = 0
    average_passengers = 0

    line = input()
    while line != "Finish":
        passengers_count = int(line)
        counter += 1
        sum_passengers += passengers_count
        average_passengers = sum_passengers / counter
        current_most_pass_per_flight = average_passengers
        current_best_company = air_company_name

        line = input()
    if current_most_pass_per_flight > most_pass_per_flight:
        most_pass_per_flight = current_most_pass_per_flight
        best_company = current_best_company

    print(f"{air_company_name}: {floor(average_passengers)} passengers.")

print(f"{best_company} has most passengers per flight: {floor(most_pass_per_flight)}")

