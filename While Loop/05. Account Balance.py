balance = 0

while True:
    command = input()

    if command == "NoMoreMoney":
        break
    money = float(command)

    if money >= 0:
        print(f"Increase: {money:.2f}")
        balance += money
    else:
        print("Invalid operation!")
        break
print(f"Total: {balance:.2f}")