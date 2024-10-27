from sys import maxsize

number = int(input())

maxNum = -maxsize
minNum = maxsize

for _ in range (number):
    currentNumber = int(input())

    if currentNumber > maxNum:
        maxNum = currentNumber

    if currentNumber < minNum:
        minNum = currentNumber


print(f"Max number: {maxNum}")
print(f"Min number: {minNum}")