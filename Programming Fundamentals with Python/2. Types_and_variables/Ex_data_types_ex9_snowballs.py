n_snowball = int(input())

previous_snowball_value = 0
highest_snowball_value = 0

for i in range(1, n_snowball+1):
    current_snowball_snow = int(input())
    current_snowball_time = int(input())
    current_snowball_quality = int(input())
    current_snowball_value = pow((current_snowball_snow / current_snowball_time), current_snowball_quality)
    if current_snowball_value > highest_snowball_value:
        highest_snowball_value = current_snowball_value
        highest_snowball_time = current_snowball_time
        highest_snowball_snow = current_snowball_snow
        highest_snowball_quality = current_snowball_quality

    previous_snowball_value = current_snowball_value

print(f"{highest_snowball_snow} : {highest_snowball_time} = {round(highest_snowball_value)} ({highest_snowball_quality})")





