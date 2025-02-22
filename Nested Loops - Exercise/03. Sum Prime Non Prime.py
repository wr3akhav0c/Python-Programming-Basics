sum_prime, non_sum_prime = 0, 0

while True:
    command = input()

    if command == "stop":
        break

    number = int(command)

    if number < 0:
        print("Number is negative.")
        continue

    is_prime = True

    for num in range(2, number):

        if number % num == 0:
            is_prime = False
            break

    if is_prime:
        sum_prime += number
    else:
        non_sum_prime += number

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {non_sum_prime}")