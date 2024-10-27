start = int(input())
final = int(input())
magic_number = int(input())

counter = 0
condition = False

for x in range (start, final + 1):
    for y in range (start, final + 1):
        counter += 1
        if x + y == magic_number:
            print(f"Combination N:{counter} ({x} + {y} = {magic_number})")
            condition = True
            break

    if condition:
        break

else:
    print(f"{counter} combinations - neither equals {magic_number}")