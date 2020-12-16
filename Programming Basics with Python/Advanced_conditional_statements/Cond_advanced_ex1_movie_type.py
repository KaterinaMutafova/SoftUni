movie_type = input()
row_count = int(input())
column_count = int(input())

seats_count = row_count * column_count
movie_type_lv = 0
#Premiere = 12
#Normal = 7.50
#Discount = 5


if movie_type == "Premiere":
    movie_type_lv = 12
elif movie_type == "Normal":
    movie_type_lv = 7.5
elif movie_type == "Discount":
    movie_type_lv = 5

money_gain_full = movie_type_lv * seats_count

print(f"{money_gain_full:.2f} leva")

