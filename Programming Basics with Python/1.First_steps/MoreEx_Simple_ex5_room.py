w_side_length_m = float(input())   #length
h_side_width_m = float(input())   #width

#3 <= h_side
#h_side <= w_side
#w_side <= 100
#3 <= h <= w <= 100

#logic
num_desks_width = (h_side_width_m - 1) //0.7
num_desks_length = w_side_length_m // 1.2
all_desks = num_desks_length * num_desks_width - 3

print(all_desks)

