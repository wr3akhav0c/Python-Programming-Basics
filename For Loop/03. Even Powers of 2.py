n = int(input())

for current_number in range (n + 1):
    if current_number % 2 == 0:
        print(2 ** current_number)