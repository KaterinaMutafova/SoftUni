text = input()
n_times = int(input())


def repeat_str(str_value, repeat_times):
    result = ""
    for time in range(repeat_times):
        result += str_value
    return result


print(f"{repeat_str(text, n_times)}")


#THE SAME THING AS:
# text = input()
# n_times = int(input())
#
#
# def repeat_str(str_value, repeat_times):
#     result = ""
#     for time in range(repeat_times):
#         result = "" + str_value
#         print(f"{result}", end="")
#
#
# repeat_str(text, n_times)

