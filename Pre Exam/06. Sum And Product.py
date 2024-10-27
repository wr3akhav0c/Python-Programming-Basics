n = int(input())

is_combination = False

for a in range(1, 10):
    for b in range(9, a -1, -1):
        for c in range(0, 10):
            for d in range(9, c - 1, -1):
                sum_all = a + b + c + d
                mult_all = a * b * c * d

                if sum_all == mult_all and n % 10 == 5:
                    print(f"{a}{b}{c}{d}")
                    is_combination = True
                    break

                if sum_all != 0 and mult_all // sum_all == 3 and n % 3 == 0:
                    # dcba
                    reversed_number = d * 1000 + c * 100 + b * 10 + a
                    print(reversed_number)
                    is_combination = True
                    break

            if is_combination:
                break
        if is_combination:
            break
    if is_combination:
        break

if not is_combination:
    print("Nothing found")
