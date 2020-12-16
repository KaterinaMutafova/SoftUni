#Първият ред съдържа думата &quot;leap&quot; (високосна година) или &quot;normal&quot; (невисокосна);
#Вторият ред съдържа цялото число p – брой празници в годината (които не са събота и неделя);
#Третият ред съдържа цялото число h – брой уикенди, в които Влади си пътува до родния град.

import math
year_type = input()
holiday_play = int(input())
weekends_home = int(input())

free_weekends_sf = (3 / 4) * (48 - weekends_home)
holiday_play = (2 / 3) * holiday_play

vol_days = holiday_play + weekends_home + free_weekends_sf

if year_type == "leap":
    vol_days += 0.15 * vol_days

print(math.floor(vol_days))




