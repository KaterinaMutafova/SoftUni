#Mоканени сте на 30-ти рожден ден, на който рожденикът черпи с огромна торта. Той обаче не знае колко
#парчета могат да си вземат гостите от нея. Вашата задача е да напишете програма, която изчислява броя на
#парчетата, които гостите са взели преди тя да свърши. Ще получите размерите на тортата (широчина и
#дължина – цели числа и след това на всеки ред, до получаване на командата &quot;STOP&quot; или докато не свърши
#тортата, броят на парчетата, които гостите вземат от нея. Всяко парче торта е с размер 1х1 см.
#Да се отпечата на конзолата един от следните редове:
# &quot;{брой парчета} pieces are left.&quot; - ако стигнете до STOP и не са свършили парчетата торта;
# &quot;No more cake left! You need {брой недостигащи парчета} pieces more.&quot;

width = int(input())
length = int(input())
line = input()

area = width * length
pieces_area = 1 * 1
count_pieces = area / pieces_area
count_not_enough = 0
count_left = 0

is_eaten = False

while line != "STOP":
    count_taken = int(line)
    count_pieces -= count_taken
    if count_pieces <= 0:
        count_pieces = abs(count_pieces)
        is_eaten = True
        break

    line = input()

if line == "Stop" and count_pieces > 0:
    is_eaten = True

if is_eaten:
    print(f"No more cake left! You need {round(count_pieces)} pieces more.")
else:
    print(f"{round(count_pieces)} pieces are left.")
