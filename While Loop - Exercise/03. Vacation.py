money_for_vacation = float(input())
money_available = float(input())

spend_counter = 0
days_counter = 0

while True:
    command = input()
    amount = float(input())
    days_counter += 1

    if command == "spend":
        spend_counter += 1
        money_available -= amount
        if money_available < 0:
            money_available = 0

        if spend_counter == 5:
            print("You can't save the money.")
            print(days_counter)
            break

    elif command == "save":
        spend_counter = 0
        money_available += amount

        if money_available >= money_for_vacation:
            print(f"You saved the money for {days_counter} days.")
            break
