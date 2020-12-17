# def perfect_number(n):
#     divisor = []
#     for num in range(1, n):
#         if n % num == 0:
#             divisor.append(num)
#     if sum(divisor) == n:
#         return True
#     return False
#
#
# number = int(input())
# if perfect_number(number):
#     print("We have a perfect number!")
# else:
#     print("It's not so perfect.")

list_a = [1, 2, 3, 4, 5, 5, 5]

print(list_a.index(5, 6))
