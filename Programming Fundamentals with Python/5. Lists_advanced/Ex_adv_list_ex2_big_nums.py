list_numbers = input().split()

list_numbers.sort(reverse=True)

for num in list_numbers:
    print(f"{num}", end="")






# turn string to  a list of int

# list_numbers = list(map(lambda el: int(el), list_numbers))

# Splitting of the two-digit numbers and creating a list of one digit integers
# 1 - from list of  int to string: with join str(list_numbers),
# 2 - turn string to list of integers

# list_numbers = list(map(int,str(''.join(str(x) for x in list_numbers))))

# sort and  order the  single-digit numbers

# single integers in a list are concatenated in one integer outside a  list
# 1.join integers in the  list



