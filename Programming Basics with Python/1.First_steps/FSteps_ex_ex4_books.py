#1. Брой страници в текущата книга – цяло число;
#2. Страници, които може да прочита за 1 час – цяло число;
#3. Броя на дните, за които трябва да прочете книгата – цяло число;

pages_book = int(input())
page_per_hour = int(input())
days_for_reading = int(input())


hours_per_day = float((pages_book / page_per_hour)/days_for_reading)

print(hours_per_day)
