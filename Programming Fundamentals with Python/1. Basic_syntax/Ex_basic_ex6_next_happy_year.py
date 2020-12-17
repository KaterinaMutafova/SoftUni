year_num = int(input())

while True:
    year_num += 1
    if len(set(str(year_num))) == len(str(year_num)):
        print(year_num)
        break
    else:
        continue




    
