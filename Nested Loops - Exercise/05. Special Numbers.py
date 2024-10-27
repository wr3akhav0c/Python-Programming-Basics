start = 1111
end = 10_000

number = int(input())

for num in range(start, end):     # 1111 ->
    for digit in str(num):        # str(num) -> '1111' -> '1' -> '1' -> '1' -> '1'

        if digit == '0':
            break

        if number % int(digit) != 0:
            break
    else:
        print(num, end =' ')