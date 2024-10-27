bad_grades = int(input())
average_score = 0
number_of_problems = 0
failed_grades = 0
total_grades = 0
last_task = ""

while failed_grades < bad_grades:
    task_name = input()
    if task_name == "Enough":
        break

    task_grade = int(input())
    if task_grade <= 4:
        failed_grades += 1
    total_grades += task_grade
    number_of_problems += 1
    last_task = task_name

if task_name == "Enough":
    if number_of_problems > 0:
        average_score = total_grades / number_of_problems
        print(f"Average score: {total_grades/number_of_problems:.2f}")
        print(f"Number of problems: {number_of_problems}")
        print(f"Last problem: {last_task}")
else:
    print(f"You need a break, {failed_grades} poor grades.")