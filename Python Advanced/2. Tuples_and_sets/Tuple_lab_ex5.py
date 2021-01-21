def is_vip(g):
    return g[0].isdigit()

def separate_guests(not_a):
    vip_guest = []
    reg_guest = []
    for g in not_a:
        if is_vip(g):
            vip_guest.append(g)
        else:
            reg_guest.append(g)
    return (sorted(vip_guest), sorted(reg_guest))


def get_result(not_a):
    (vip_guest, reg_guest) = separate_guests(not_a)
    for i in vip_guest:
        print(i)

    for r in reg_guest:
        print(r)


num_guests = int(input())

invited_guests = []
arrived = []

for guest in range(num_guests):
    invited_guests.append(input())


arrive_guest = input()
while not arrive_guest == "END":
    arrived.append(arrive_guest)

    arrive_guest = input()

invited_guests = set(invited_guests)
arrived = set(arrived)

not_arrived = invited_guests.symmetric_difference(arrived)
print(len(not_arrived))


get_result(not_arrived)









