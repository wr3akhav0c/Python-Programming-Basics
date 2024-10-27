width = int(input())
length = int(input())

cake_size = width * length

count_pieces = 0
result = ""

while cake_size > count_pieces:
    pieces = input()

    if pieces == "STOP":
        result = f"{cake_size - count_pieces} pieces are left."
        break

    count_pieces += int(pieces)

else:
    result = f"No more cake left! You need {count_pieces - cake_size} pieces more."

print(result)