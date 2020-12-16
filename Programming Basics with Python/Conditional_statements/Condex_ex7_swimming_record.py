#1. Рекордът в секунди – реално число;
#2. Разстоянието в метри – реално число;
#3. Времето в секунди, за което плува разстояние от 1 м. - реално число.

world_record_sec = float(input())
distance_m = float(input())
time_sec_per_1m_ivan = float(input())

#Да се напише програма, която изчислява дали се е
#справил със задачата, като се има предвид, че: съпротивлението на водата го забавя на всеки 15 м. с 12.5
#секунди. Когато се изчислява колко пъти Иванчо ще се забави, в резултат на съпротивлението на водата,
#резултатът трябва да се закръгли надолу до най-близкото цяло число.
#Да се изчисли времето в секунди, за което Иванчо ще преплува разстоянието и разликата спрямо
#Световния рекорд.

time_sec_ivan_per_distance = time_sec_per_1m_ivan * distance_m
added_time_sec = (distance_m//15) * 12.5
record_ivan_and_added_time = time_sec_ivan_per_distance + added_time_sec

difference_sec = record_ivan_and_added_time - world_record_sec

if record_ivan_and_added_time < world_record_sec:
    print(f"Yes, he succeeded! The new world record is {record_ivan_and_added_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference_sec:.2f} seconds slower.")
