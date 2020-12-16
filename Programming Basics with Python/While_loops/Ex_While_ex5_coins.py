money = float(input())
coin_count = 0

#   2   1   0.50   0.20   0.10  0.5   0.2   0.1
# 10 * 1st = 10st
# 10 * 10st = 100st = 1lv

money_count_st = money * 100
while True:
    coin_count += 1
    if money_count_st >= 200:
        money_count_st -= 200
    elif money_count_st >= 100:
        money_count_st -= 100
    elif money_count_st >= 50:
        money_count_st -= 50
    elif money_count_st >= 20:
        money_count_st -= 20
    elif money_count_st >= 10:
        money_count_st -= 10
    elif money_count_st >= 5:
        money_count_st -= 5
    elif money_count_st >= 2:
        money_count_st -= 2
    elif money_count_st >= 1:
        money_count_st -= 1

    if money_count_st < 1:
        break

print(coin_count)
