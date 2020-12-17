# First, you will receive your budget.
# Then, you will receive the price for 1 kg flour.

budget = float(input())
price_flour = float(input())

# The price for 1 pack of eggs is 75% of the price for 1 kg flour.
# The price for 1l milk is 25% more than price for 1 kg flour.
# Notice, that you need 0.250l milk for one cozonac and the calculated price is for 1l.

price_1_p_eggs = 0.75 * price_flour
price_1l_milk = 1.25 * price_flour

price_025l_milk = price_1l_milk / 4

price_one_couzunac = price_flour + price_1_p_eggs + price_025l_milk
budget_left = budget
count_eggs = 0
counter = 0
count_couzunac = budget // price_one_couzunac

while budget_left > price_one_couzunac:
    budget_left -= price_one_couzunac
    counter +=1
    if counter % 3 == 0:
        count_eggs += 3
        count_eggs -= counter - 2
    else:
        count_eggs += 3

print(f"You made {round(count_couzunac)} cozonacs! Now you have {round(count_eggs)} eggs and {budget_left:.2f}BGN left.")



