puzzle = 2.60
doll = 3.00
teddyBear = 4.10
minion = 8.20
truck = 2.00

orderedToys = 0
discount = 0
totalPrice = 0

vacationPrice = float(input())
numPuzzles = int(input())
numDolls = int(input())
numTeddyBears = int(input())
numMinions = int(input())
numTrucks = int(input())

orderedToys = numPuzzles + numDolls + numTeddyBears + numMinions + numTrucks

totalPrice = (
    numPuzzles * puzzle +
    numDolls * doll +
    numTeddyBears * teddyBear +
    numMinions * minion +
    numTrucks * truck
)

if orderedToys >= 50:
    discount = totalPrice * 0.25
    totalPrice -= discount

forRent = totalPrice * 0.1
moneyLeft = totalPrice - forRent

if moneyLeft >= vacationPrice:
    moneyForVacation = moneyLeft - vacationPrice
    print(f"Yes! {moneyForVacation:.2f} lv left.")
else:
    insufficientMoney = vacationPrice - moneyLeft
    print(f"Not enough money! {insufficientMoney:.2f} lv needed.")
