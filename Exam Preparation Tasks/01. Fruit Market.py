strawberry_price = float(input()) ##per Kg
banana_quantity = float(input())
orange_quantity = float(input())
raspberry_quantity = float(input())
strawberry_quantity = float(input())

raspberry_price = strawberry_price / 2
orange_price = raspberry_price - (raspberry_price * 0.4)
banana_price = raspberry_price - (raspberry_price * 0.8)

strawberry_total = strawberry_quantity * strawberry_price
banana_total = banana_price * banana_quantity
orange_total = orange_price * orange_quantity
raspberry_total = raspberry_quantity * raspberry_price

total = strawberry_total + banana_total + orange_total + raspberry_total

print(f"{total:.2f}")