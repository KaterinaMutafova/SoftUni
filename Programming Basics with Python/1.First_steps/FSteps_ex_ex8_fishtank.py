#1. Дължина в см – цяло число
#2. Широчина в см – цяло число
#3. Височина в см – цяло число
#4. Процент зает обем – реално число

length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent_filled = float(input())

#logic
volume_dm = (length_cm * width_cm * height_cm)/1000
volume_filled = volume_dm * percent_filled
volume_water = volume_dm - (volume_filled/100)

print(volume_water)
