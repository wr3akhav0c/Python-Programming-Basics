goal = 10000
total_steps = 0

while True:
    action = input()

    if action == "Going home":
        steps = int(input())
        total_steps += steps
        if total_steps >= goal:
            print("Goal reached! Good job!")
            print(f"{total_steps-goal} steps over the goal!")
        else:
            print(f"{goal - total_steps} more steps to reach goal.")
        break
    else:
        steps = int(action)
        total_steps += steps
        if total_steps >= goal:
            print("Goal reached! Good job!")
            print(f"{total_steps-goal} steps over the goal!")
            break
