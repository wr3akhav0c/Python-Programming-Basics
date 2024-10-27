width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height

cubic_meters = 0
result = ""

while free_space > cubic_meters:
    box = input()

    if box == "Done":
        result = f"{free_space-cubic_meters} Cubic meters left."
        break

    cubic_meters += int(box)

else:
    result = f"No more free space! You need {cubic_meters - free_space} Cubic meters more."

print(result)