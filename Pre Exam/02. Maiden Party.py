love_letter = 0.60
wax_rose = 7.20
keychain = 3.60
caricature = 18.20
lucky_surprise = 22.00

maid_party_cost = float(input())
love_letter_count = int(input())
wax_rose_count = int(input())
keychain_count = int(input())
caricature_count = int(input())
lucky_surprise_count = int(input())

items_count = love_letter_count + wax_rose_count + keychain_count + caricature_count + lucky_surprise_count

cost_all = (love_letter * love_letter_count) + (wax_rose * wax_rose_count) + (keychain * keychain_count) + (caricature * caricature_count) + (lucky_surprise_count * lucky_surprise)

if items_count >= 25:
    cost_all = cost_all - (cost_all * 0.35)

hosting = 0.1

price_after_hosting = cost_all - (cost_all * hosting)

if price_after_hosting >= maid_party_cost:
    money_left = price_after_hosting - maid_party_cost
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_needed = maid_party_cost - price_after_hosting
    print(f"Not enough money! {money_needed:.2f} lv needed.")