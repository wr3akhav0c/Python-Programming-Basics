num_student = 0
num_standard = 0
num_kid = 0

result = ""

while True:
    movie_name = input()

    if movie_name == "Finish":
        break

    capacity = int(input())
    sold_tickets = 0

    while sold_tickets < capacity:
        ticket_type = input()

        if ticket_type == "End":
            break
        if ticket_type == "student":
            num_student += 1
        elif ticket_type == "standard":
            num_standard += 1
        elif ticket_type == "kid":
            num_kid +=1

        sold_tickets += 1

    result += f"{movie_name} - {sold_tickets / capacity * 100:.2f}% full.\n"

total_tickets = num_student + num_standard + num_kid
result += f"Total tickets: {total_tickets}\n" \
          f"{num_student / total_tickets * 100:.2f}% student tickets.\n" \
          f"{num_standard / total_tickets * 100:.2f}% standard tickets.\n" \
          f"{num_kid / total_tickets * 100:.2f}% kids tickets."

print(result)