rose = 5.00
dahlia = 3.80
tulip = 2.80
narcis = 3.00
gladiola = 2.50
price = 0

flower = input()
quantity = int(input())
budget = int(input())

if flower == "Roses":
    price = rose
elif flower == "Dahlias":
    price = dahlia
elif flower == "Tulips":
    price = tulip
elif flower == "Narcissus":
    price = narcis
elif flower == "Gladiolus":
    price = gladiola

total = price * quantity

if flower == "Roses":
    if quantity > 80:
        total = total - (total * 0.1)
elif flower == "Dahlias":
    if quantity > 90:
        total = total - (total * 0.15)
elif flower == "Tulips":
    if quantity > 80:
        total = total - (total * 0.15)
elif flower == "Narcissus":
    if quantity < 120:
        total = total + (total * 0.15)
elif flower == "Gladiolus":
    if quantity < 80:
        total = total + (total * 0.2)

if budget >= total:
    moneyLeft = budget - total
    print(f"Hey, you have a great garden with {quantity} {flower} and {moneyLeft:.2f} leva left.")
else:
    neededMoney = total - budget
    print(f"Not enough money, you need {neededMoney:.2f} leva more.")