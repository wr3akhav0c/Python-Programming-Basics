decorPercent = 0.10
discountThreshhold = 150
discountPercent = 0.10

budgetMovie = float(input())
statists = int(input())
priceClothesForStatist = float(input())

decorPrice = budgetMovie * decorPercent
clothesPrice = statists * priceClothesForStatist

if statists > discountThreshhold:
    clothesPrice -= (clothesPrice * discountPercent)

totalSum = decorPrice + clothesPrice

if totalSum > budgetMovie:
    print("Not enough money!")
    print(f"Wingard needs {totalSum - budgetMovie:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budgetMovie - totalSum:.2f} leva left.")