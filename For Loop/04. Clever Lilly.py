
age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_saved = 0
toys_count = 0
money_from_birthdays = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        money_from_birthdays += 10 * (birthday // 2)
        money_saved += money_from_birthdays - 1
    else:
        toys_count += 1

money_saved += toys_count * toy_price

if money_saved >= washing_machine_price:
    print(f"Yes! {money_saved - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - money_saved:.2f}")
