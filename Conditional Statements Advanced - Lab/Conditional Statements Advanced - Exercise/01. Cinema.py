premiere = 12.00
normal = 7.50
discount = 5.00

projectionType = input()
rows = int(input())
columns = int(input())

income = 0

cinemaCapacity = rows * columns

if projectionType == "Premiere":
    income = cinemaCapacity * premiere
elif projectionType == "Normal":
    income = cinemaCapacity * normal
elif projectionType == "Discount":
    income = cinemaCapacity * discount

print(f"{income:.2f} leva")