singleRoom = 18.00
apartment = 25.00
presidentAp = 35.00

days = int(input())
place = input()
rating = input()

price = 0
# for calculating price per night
nights = days - 1

if place == "room for one person":
    price = singleRoom
elif place == "apartment":
    price = apartment
elif place == "president apartment":
    price = presidentAp

priceTotal = price * nights

if place == "apartment":
    if days < 10:
        priceTotal = priceTotal - (priceTotal * 0.3)
    elif 10 <= days <= 15:
        priceTotal = priceTotal - (priceTotal * 0.35)
    elif days > 15:
        priceTotal = priceTotal - (priceTotal * 0.5)
elif place == "president apartment":
    if days < 10:
        priceTotal = priceTotal - (priceTotal * 0.1)
    elif 10 <= days <= 15:
        priceTotal = priceTotal - (priceTotal * 0.15)
    elif days > 15:
        priceTotal = priceTotal - (priceTotal * 0.2)

if rating == "positive":
    priceTotal = priceTotal + (priceTotal * 0.25)
elif rating == "negative":
    priceTotal = priceTotal - (priceTotal * 0.1)

print(f"{priceTotal:.2f}")