number = int(input())
additions = 0

while True:
    currentNumber = int(input())
    additions += currentNumber

    if additions >= number:
        print(additions)
        break