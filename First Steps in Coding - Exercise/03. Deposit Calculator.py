depositedValue = int(input())
deadlineInMonths = int(input())
yearlyDepositPercent = float(input()) / 100

amountFormula = depositedValue + deadlineInMonths * ((depositedValue * yearlyDepositPercent) / 12)
print(amountFormula)