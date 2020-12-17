# Lottery tickets - invalid, match, jackpot

tickets_list = input().split(", ")
winning_symbols = ["@", "#", "$", "^"]

a = 6


def is_jackpot(ticket):
    left_half = ticket[:10]
    right_half = ticket[10:]
    if not left_half == right_half:
        return False
    for winning_symbol in winning_symbols:
        if winning_symbol * 10 == left_half:
            print(f'ticket "{ticket}" - 10{winning_symbol} Jackpot!')
            return True
    return False


def is_winning(ticket):
    left_half = ticket[0:10]
    right_half = ticket[10:20]
    for winning_symbol in winning_symbols:
        if winning_symbol * 6 in left_half and winning_symbol * 6 in right_half:
            count_left = left_half.count(winning_symbol)
            count_right = right_half.count(winning_symbol)
            count = min(count_left, count_right)
            print(f'ticket "{ticket}" - {count}{winning_symbol}')
            return True
    return False


for t in tickets_list:
    ticket = t.strip()

    if not len(ticket) == 20:
        print("invalid ticket")
        continue
    if is_jackpot(ticket):
        continue
    if is_winning(ticket):
        continue

    print(f"ticket \"{ticket}\" - no match")








# for ticket in tickets_list:
#     ticket = ticket.strip()
#     left_half = ticket[:10]
#     right_half = ticket[10:]
#
#     counter_left = 0
#     counter_right = 0
#
#     if not len(ticket) == 20:
#         print("invalid ticket")
#         continue
#
#     for el in left_half:
#         if el == "@" or el == "#" or el == "$" or el == "^":
#             counter_left += 1
#             symbol_left = el
#
#     for elem in right_half:
#         if elem == "@" or elem == "#" or elem == "$" or elem == "^":
#             counter_right += 1
#             symbol_right = elem
#
#
#     if counter_left == counter_right and 6 <= counter_left <= 9 and symbol_left == symbol_right:
#         print(f"ticket \"{ticket}\" - {counter_left}{symbol_left}")
#     elif counter_left == counter_right and counter_left == 10  and symbol_left == symbol_right:
#         print(f"ticket \"{ticket}\" - {counter_left}{symbol_left} Jackpot!")
#     elif counter_left != counter_right or counter_left < 6:
#         print(f"ticket \"{ticket}\" - no match")







