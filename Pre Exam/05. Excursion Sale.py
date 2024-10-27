sea = 680.00
mountain = 499.00
profit = 0

sea_vacations_count = int(input())
mountain_vacations_count = int(input())

# packages_total_count = sea_vacations_count + mountain_vacations_count

while True:

    vacation_type = input()
    if vacation_type == "sea" and sea_vacations_count > 0:
        profit += sea
        sea_vacations_count -= 1

    if vacation_type == "mountain" and mountain_vacations_count > 0:
        profit += mountain
        mountain_vacations_count -= 1

    if vacation_type == "Stop":
        break

    if mountain_vacations_count == 0 and sea_vacations_count == 0:
        print(f"Good job! Everything is sold.")
        break

print(f"Profit: {round(profit)} leva.")

