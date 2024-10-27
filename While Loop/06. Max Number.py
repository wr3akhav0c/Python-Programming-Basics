max = float('-inf')

while True:
    command = input()
    if command == "Stop":
        print(max)
        break
    else:
        money = int(command)
        if money > max:
            max = money