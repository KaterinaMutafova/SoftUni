def positive_negative(nums_list):
    positive_list = list(filter(lambda x: x > 0, nums_list))
    negative_list = list(filter(lambda x: x < 0, nums_list))
    print(sum(negative_list))
    print(sum(positive_list))
    if abs(sum(negative_list)) > sum(positive_list):
        print(f"The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = [int(el) for el in input().split()]
positive_negative(numbers)
