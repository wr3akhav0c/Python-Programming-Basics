import math

minimum_km = 1000
total_km = 0

days_training = int(input())
km_first_day = float(input())
total_km = km_first_day

for days in range(1, days_training + 1):
    percentage_km_each_day = float(input())
    km_first_day += km_first_day * (percentage_km_each_day / 100)
    total_km += km_first_day

if total_km >= minimum_km:
    km_more = total_km - minimum_km
    print(f"You've done a great job running {math.ceil(km_more)} more kilometers!")
else:
    km_needed = minimum_km - total_km
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(km_needed)} more kilometers")

