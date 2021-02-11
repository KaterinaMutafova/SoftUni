count = int(input())

intersections = []

for iteration in range(count):
    intersection_1, intersection_2 = input().split("-")
    start_num, end_num = [int(el) for el in intersection_1.split(",")]
    first_range = range(start_num, end_num + 1)
    start_num2, end_num2 = [int(el) for el in intersection_2.split(",")]
    second_range = range(start_num2, end_num2 +1)
    intersection = set(first_range).intersection(set(second_range))
    intersections.append(intersection)

longest = sorted(intersections, key=lambda x: -len(x))[0]
print(f"Longest intersection is {list(longest)} with length {len(longest)}")




