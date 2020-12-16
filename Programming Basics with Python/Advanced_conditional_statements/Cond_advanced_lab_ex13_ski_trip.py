#Първи ред - дни за престой - цяло число;
#Втори ред - вид помещение - &quot;room for one person&quot;, &quot;apartment&quot; или &quot;president apartment&quot;;
#Трети ред - оценка - &quot;positive&quot; или &quot;negative&quot;.

days = int(input())
room_type = input()
mark = input()

nights = days - 1
price_per_night = 0
discount = 0
whole_sum = nights * price_per_night - discount

if room_type == "room for one person":
    price_per_night = 18
    discount = 0
    whole_sum = nights * price_per_night

elif room_type == "apartment":
    price_per_night = 25
    whole_sum = nights * price_per_night
    if days < 10:
        discount = whole_sum * 0.3
    elif 10 <= days <= 15:
        discount = whole_sum * 0.35
    elif days > 15:
        discount = whole_sum * 0.5

elif room_type == "president apartment":
    price_per_night = 35
    whole_sum = nights * price_per_night
    if days < 10:
        discount = whole_sum * 0.1
    elif 10 <= days <= 15:
        discount = whole_sum * 0.15
    elif days > 15:
        discount = whole_sum * 0.2

whole_sum = whole_sum - discount

if mark == "positive":
    whole_sum = whole_sum + 0.25 * whole_sum
else:
    whole_sum = whole_sum - 0.1 * whole_sum

print(f"{whole_sum:.2f}")

