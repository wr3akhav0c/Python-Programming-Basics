budget = float(input())
season = input()
cost = 0
destination = ""
accommodation = ""

if budget <= 100:
    if season == "summer":
        accommodation = "Camp"
        cost = budget * 0.3
        print(f"Somewhere in Bulgaria")
        print(f"{accommodation} - {cost:.2f}")
    elif season == "winter":
        accommodation = "Hotel"
        cost = budget * 0.7
        print(f"Somewhere in Bulgaria")
        print(f"{accommodation} - {cost:.2f}")
elif 100 < budget <= 1000:
    if season == "summer":
        accommodation = "Camp"
        cost = budget * 0.4
        print(f"Somewhere in Balkans")
        print(f"{accommodation} - {cost:.2f}")
    elif season == "winter":
        accommodation = "Hotel"
        cost = budget * 0.8
        print(f"Somewhere in Balkans")
        print(f"{accommodation} - {cost:.2f}")
elif budget > 1000:
    cost = budget * 0.9
    accommodation = "Hotel"
    print(f"Somewhere in Europe")
    print(f"{accommodation} - {cost:.2f}")