budget = float(input())
destination = input()
season = input()
days = int(input())

cost = 0

if season == "Winter" and destination == "Dubai":
    cost = 45000
elif season == "Winter" and destination =="Sofia":
    cost = 17000
elif season == "Winter" and destination =="London":
    cost = 24000

if season == "Summer" and destination == "Dubai":
    cost = 40000
elif season == "Summer" and destination == "Sofia":
    cost = 12500
elif season == "Summer" and destination == "London":
    cost = 20250

include_days = cost * days

if destination == "Dubai":
    include_days = include_days - (include_days * 0.3)

if destination == "Sofia":
    include_days = include_days + (include_days * 0.25)

if budget >= include_days:
    moneyLeft = budget - include_days
    print(f"The budget for the movie is enough! We have {moneyLeft:.2f} leva left!")
elif budget < include_days:
    moneyNeeded = include_days - budget
    print(f"The director needs {moneyNeeded:.2f} leva more!")