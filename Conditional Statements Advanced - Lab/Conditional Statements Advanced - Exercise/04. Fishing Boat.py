budget = int(input())
season = input()
fishermen = int(input())

rent = 0

if season == "Spring":
    rent = 3000
elif season in ("Summer", "Autumn"):
    rent = 4200
elif season == "Winter":
    rent = 2600

if fishermen <= 6:
    rent = rent - (rent * 0.1)
elif 7 < fishermen <= 11:
    rent = rent - (rent * 0.15)
elif fishermen >= 12:
    rent = rent - (rent * 0.25)

if fishermen % 2 == 0:
    if season != "Autumn":
        rent = rent - (rent * 0.05)

if budget >= rent:
    moneyLeft = budget - rent
    print(f"Yes! You have {moneyLeft:.2f} leva left.")
else:
    moneyNeedeed = rent - budget
    print(f"Not enough money! You need {moneyNeedeed:.2f} leva.")