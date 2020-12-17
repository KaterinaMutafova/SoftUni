from math import floor
party_size = int(input())
days = int(input())
coin_count = 0

for day in range(1, days+1):
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5
    coin_count += 50
    coin_count = coin_count - party_size * 2
    if day % 3 == 0:
        coin_count = coin_count - party_size * 3
    if day % 5 == 0:
        coin_count += 20 * party_size
        if day % 3 == 0:
            coin_count = coin_count - party_size * 2

left_coins = coin_count
coin_per_companion = coin_count / party_size

print(f"{party_size} companions received {floor(coin_per_companion)} coins each.")



