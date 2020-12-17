cards = input().split()


def check_matching_cards(list_cards, i_1, i_2, counter_round):
    if list_cards[i_1] == list_cards[i_2]:
        matching_card = list_cards[i_1]
        print(f"Congrats! You have found matching elements - {list_cards[i_1]}!")
        list_cards.remove(matching_card)
        list_cards.remove(matching_card)
        return cards
    if i_1 == i_2 or i_1 not in range(len(list_cards)) or i_2 not in range(len(list_cards)):
        print("Invalid input! Adding additional elements to the board")
        index_to_insert = len(list_cards) // 2
        new_card = f"-{counter_round}a"
        list_cards.insert(index_to_insert, new_card)
        list_cards.insert(index_to_insert, new_card)
        return cards
    print("Try again!")
    return cards


command = input()
round = 0

while not command == "end":
    index_1, index_2 = [int(el) for el in command.split()]
    round += 1
    cards = check_matching_cards(cards, index_1, index_2, round)

    if len(cards) == 0:
        print(f"You have won in {round} turns!")
        exit(0)
    command = input()


print(f"Sorry you lose :(")
print(f"{' '.join(cards)}")



