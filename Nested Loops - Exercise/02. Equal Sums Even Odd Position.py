first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number + 1):
    even_sum = 0
    odd_sum = 0

    for index, num in enumerate(str(number)):

        if index % 2 == 0:
            even_sum += int(num)
        else:
            odd_sum += int(num)

    if even_sum == odd_sum:
        print(number, end =' ')