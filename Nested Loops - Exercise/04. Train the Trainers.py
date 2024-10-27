judges = int(input())

total_sum_grades, total_count_grades = 0, 0
result = ""

while True:
    presentation_name = input()

    if presentation_name == "Finish":
        break

    current_sum_grades = 0

    for _ in range(judges):
        grade = float(input())

        current_sum_grades += grade

    result += f"{presentation_name} - {current_sum_grades / judges:.2f}.\n"
    total_sum_grades += current_sum_grades
    total_count_grades += judges

result += f"Student's final assessment is {total_sum_grades / total_count_grades:.2f}."
print(result)