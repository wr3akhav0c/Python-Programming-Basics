budget = float(input())
nights_count = int(input())
price_per_night = float(input())
percent_additional_costs = int(input())

if nights_count > 7:
    price_per_night = price_per_night - (price_per_night * 0.05)

price_for_trip = budget - (budget * (percent_additional_costs / 100))

if price_for_trip >= (nights_count * price_per_night):
    money_left_for_trip = price_for_trip - (nights_count * price_per_night)
    print(f"Ivanovi will be left with {money_left_for_trip:.2f} leva after vacation.")
elif price_for_trip < (nights_count * price_per_night):
    money_needed = (nights_count * price_per_night) - price_for_trip
    print(f"{money_needed:.2f} leva needed.")