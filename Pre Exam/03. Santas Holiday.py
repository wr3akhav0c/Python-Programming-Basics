
room_for_one_person = 18.00    # prices per NIGHT
apartment = 25.00
president_apartment = 35.00

days_stay = int(input())
accommodation_type = input()
rating = input()

nights_stay = days_stay - 1
price = 0

if accommodation_type == "room for one person":
    price = room_for_one_person
elif accommodation_type == "apartment":
    price = apartment
elif accommodation_type == "president apartment":
    price = president_apartment

price_total = price * nights_stay

if accommodation_type == "apartment":
    if days_stay < 10:
        price_total = price_total - (price_total * 0.3)
    elif 10 <= days_stay <= 15:
        price_total = price_total - (price_total * 0.35)
    elif days_stay > 15:
        price_total = price_total - (price_total * 0.5)

elif accommodation_type == "president apartment":
    if days_stay < 10:
       price_total = price_total - (price_total * 0.1)
    elif 10 <= days_stay <= 15:
       price_total = price_total - (price_total * 0.15)
    elif days_stay > 15:
       price_total = price_total - (price_total * 0.2)

if rating == "positive":
    price_total = price_total + (price_total * 0.25)
elif rating == "negative":
    price_total = price_total - (price_total * 0.1)

print(f"{price_total :.2f}")


