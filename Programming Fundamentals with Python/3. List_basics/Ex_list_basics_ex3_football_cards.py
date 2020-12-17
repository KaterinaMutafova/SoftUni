cards = input()

team_a = list()
team_b = list()
game_off = False

for i in range(1, 12):
    team_a.append(str(i))
    team_b.append(str(i))

list_cards = cards.split(" ")
for i in range(len(list_cards)):
    cards_cut = list_cards[i].split("-")
    if len(team_a) < 7 or len(team_b) < 7:
        game_off = True
        break
    if cards_cut[0] == "A":
        if cards_cut[1] not in team_a:
            pass
        else:
            team_a.remove(cards_cut[1])

    elif cards_cut[0] == "B":
        if cards_cut[1] not in team_b:
            pass
        else:
            team_b.remove(cards_cut[1])

if game_off:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
    print("Game was terminated")
else:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")







# cards = input()
#
# team_a = list()
# team_b = list()
#
# for i in range(1, 12):
#     team_a.append(str(i))
#     team_b.append(str(i))
#
# list_cards = cards.split(" ")
#
# for j in range(len(list_cards)):
#     if "A" in list_cards[j][0]:
#         if list_cards[j][2] in team_a:
#             team_a.remove(list_cards[j][2])
#     elif "B" in list_cards[j][0]:
#         if list_cards[j][2] in team_b:
#             team_b.remove(list_cards[j][2])
#
# print(team_a)
# print(team_b)
