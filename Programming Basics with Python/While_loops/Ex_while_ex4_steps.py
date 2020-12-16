line = input()
steps_goal = 10000
sum_steps = 0
goal_is_reached = False

while line != "Going home":
    steps = int(line)
    sum_steps += steps

    if sum_steps >= steps_goal:
        goal_is_reached = True
        break

    line = input()
if line == "Going home":
    more_steps = int(input())
    sum_steps += more_steps
    diff = sum_steps - steps_goal
    if sum_steps > steps_goal:
        goal_is_reached = True
    elif sum_steps < steps_goal:
        goal_is_reached = False

if goal_is_reached:
    print(f"Goal reached! Good job!")
    if sum_steps > steps_goal:
        diff = sum_steps - steps_goal
        print(f"{diff} steps over the goal!")
elif not goal_is_reached:
    diff = steps_goal - sum_steps
    print(f"{abs(diff)} more steps to reach goal.")