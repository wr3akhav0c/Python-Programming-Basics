month = input()
nights = int(input())
studioPrice = 0
apartmentPrice = 0

if month in ("May", "October"):
    studioPrice = 50
    apartmentPrice = 65
elif month in ("June", "September"):
    studioPrice = 75.20
    apartmentPrice = 68.70
elif month in ("July", "August"):
    studioPrice = 76
    apartmentPrice = 77

priceForStudio = studioPrice * nights
priceForApartment = apartmentPrice * nights

##discounts
if 7 < nights <= 14 and month in ("May", "October"):
    priceForStudio = priceForStudio - (priceForStudio * 0.05)
elif nights > 14 and month in ("May", "October"):
    priceForStudio = priceForStudio - (priceForStudio * 0.3)

if nights > 14 and month in ("June", "September"):
    priceForStudio = priceForStudio - (priceForStudio * 0.2)

if nights > 14:
    priceForApartment = priceForApartment - (priceForApartment * 0.1)

print(f"Apartment: {priceForApartment:.2f} lv.")
print(f"Studio: {priceForStudio:.2f} lv.")