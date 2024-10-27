min = float('inf')

while True:
    command = input()
    if command == "Stop":
        print(min)
        break
    else:
        money = int(command)
        if money < min:
            min = money