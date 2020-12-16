
# Торта – цената ѝ е 20% от наема на залата
# Напитки – цената им е 45% по-малко от тази на тортата
# Аниматор – цената му е 1/3 от цената за наема на залата

rent = float(input())

#logic
cake = rent * (20/100)
drinks = cake - (cake * (45/100))
animator = 1/3 * rent

whole_sum = rent + cake + drinks + animator

print(whole_sum)


