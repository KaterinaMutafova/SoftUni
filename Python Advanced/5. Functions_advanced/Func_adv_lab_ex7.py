def calc_comb(names, n, combinations = []):
    if len(combinations) == n:
        print(', '.join(combinations))
        return
    for i in range(len(names)):
        current_name = names[i]
        combinations.append(current_name)
        calc_comb(names[i+1:], n, combinations)
        combinations.pop()


names = input().split(", ")
n = int(input())

calc_comb(names, n)