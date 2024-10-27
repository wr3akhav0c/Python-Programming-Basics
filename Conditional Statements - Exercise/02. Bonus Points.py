inputNumber = int(input())
bonus = 0

if inputNumber < 101:
    bonus = 5
elif 101 < inputNumber < 1000:
    bonus = 0.2 * inputNumber
else:
    bonus = 0.1 * inputNumber

if inputNumber % 2 == 0:
    bonus += 1
elif inputNumber % 10 == 5:
    bonus += 2

print(bonus)
print(bonus + inputNumber)