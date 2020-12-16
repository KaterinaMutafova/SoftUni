#На първия ред е месецът – May, June, July, August, September или October;
#На втория ред е броят на нощувките – цяло число.

month = input()
nights = int(input())

room = "somewhere"
nights_lv_apart = 0
nights_lv_stud = 0


if month == "May" or month == "October":
    nights_lv_stud = 50
    nights_lv_apart = 65

    if 7 < nights <= 14:
        nights_lv_stud = 0.95 * nights_lv_stud
    elif nights > 14:
        nights_lv_stud = 0.7 * nights_lv_stud
        nights_lv_apart = 0.9 * nights_lv_apart
    nights_lv_apart = nights_lv_apart * nights
    nights_lv_stud = nights_lv_stud * nights


elif month == "June" or month == "September":
    nights_lv_stud = 75.2
    nights_lv_apart = 68.7
    nights_lv_apart = nights_lv_apart * nights
    nights_lv_stud = nights_lv_stud * nights
    if nights > 14:
        nights_lv_stud = 0.8 * nights_lv_stud
        nights_lv_apart = 0.9 * nights_lv_apart


elif month == "July" or month == "August":
    nights_lv_stud = 76
    nights_lv_apart = 77
    nights_lv_apart = nights_lv_apart * nights
    nights_lv_stud = nights_lv_stud * nights
    if nights > 14:
        nights_lv_apart = 0.9 * nights_lv_apart

#За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
#За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
#За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
#За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.

print(f"Apartment: {nights_lv_apart:.2f} lv.")
print(f"Studio: {nights_lv_stud:.2f} lv.")

