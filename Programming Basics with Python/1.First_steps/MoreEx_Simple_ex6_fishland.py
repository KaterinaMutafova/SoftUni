#Първи ред – цена на скумрията на килограм. Реално число в интервала [0.00…40.00]
#Втори ред – цена на цацата на килограм. Реално число в интервала [0.00…30.00]
#Трети ред – килограма паламуд. Реално число в интервала [0.00…50.00]
#Четвърти ред – килограма сафрид. Реално число в интервала [0.00… 70.00]
#Пети ред – килограма миди. Цяло число в интервала [0 ... 100]

skumria_lv_per_kg = float(input())
caca_lv_per_kg = float(input())
palamud_amount = float(input())
safrid_amount = float(input())
midi_amount = int(input())

#logic
#Паламуд – 60% по-скъп от скумрията
#Сафрид – 80% по-скъп от цацата
#Миди – 7.50 лв. за килограм

palamud_lv_per_kg = 0.6 * skumria_lv_per_kg + skumria_lv_per_kg
safrid_lv_per_kg = 0.8 * caca_lv_per_kg + caca_lv_per_kg
midi_lv_per_kg = 7.50

palamud_total_lv = palamud_lv_per_kg * palamud_amount
safrid_total_lv = safrid_lv_per_kg * safrid_amount
midi_total_lv = midi_lv_per_kg * midi_amount

total_lv = palamud_total_lv + safrid_total_lv + midi_total_lv

print(f"{total_lv:.2f}")

